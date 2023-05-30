from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProblemForm, ReviewForm
from .models import Problem, Review
from .tasks import remove_unused_tags
from .utils import OrderedCounter


# Create your views here.
def detail(request, pk):
    problem = get_object_or_404(
        Problem.objects.prefetch_related(
            'tags',
            'review_set__tags',
            'review_set__comment_set__tags',
        ),
        pk=pk
    )
    # print(problem.tags.all())
    # c = OrderedCounter(problem.objects.tags + problem.review_set.tags + problem.review_set.comment_set.tags)
    # print(c)
    context = {
        'problem': problem,
    }
    return render(request, 'reviews/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ProblemForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            form.save_m2m()
            return redirect('reviews:detail', problem.pk)
        else:
            print(form.error)
            return redirect('/')
    else:
        form = ProblemForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


def update(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == 'POST':
        form = ProblemForm(data=request.POST, instance=problem)
        if form.is_valid():
            form.save_m2m()
            form.save()
            return redirect('reviews:detail', problem.pk)
        print('not valid')
    else:
        form = ProblemForm(instance=problem)
    context = {
        'form': form,
    }
    return render(request, 'reviews/update.html', context)


def delete(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    if request.user == problem.user:
        problem.delete()
        remove_unused_tags.delay(problem)
        return redirect('/')  # 추후 스터디 앱의 메인 페이지로 redirect하도록 수정
    # 권한이 없는 페이지 만들기?
    # 왔던 곳으로 되돌아가게 하려면?
    return redirect('reviews:detail', pk)
    

def review_create(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user, review.problem = request.user, problem
            review.save()
            return redirect('reviews:detail', problem.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
        'problem_pk': pk,
    }
    return render(request, 'reviews/review_create.html', context)


def review_update(request, pk, review_pk):
    problem = get_object_or_404(Problem, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(data=request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', problem.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'reviews/review_update.html', context)


def review_delete(request, pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        return redirect('/')
    return redirect('reviews:detail', pk)