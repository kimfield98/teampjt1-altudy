from django.shortcuts import render, get_list_or_404
from studies.models import Study, Studying
from django.db.models import Count
from studies.models import LANGUAGE_CHOICES

def main(request):
    # 가입 중인 스터디
    # 스터디에서 접근 시 {for-each}.study.title로 접근
    if request.user.is_authenticated:
        studyings = Studying.objects.filter(user=request.user)
    else:
        studyings = None
    # 최신 스터디 16개
    latest_studies = Study.objects.annotate(
        member_num=Count('studying_users')
        ).order_by('-created_at')[:16]
    
    context = {
        'studyings': studyings,
        'latest_studies': latest_studies,
        'LANGUAGE_CHOICES': LANGUAGE_CHOICES,
    }
    return render(request, 'main.html', context)