from django import forms
from django_tuieditor.widgets import MarkdownEditorWidget
from django_tuieditor.fields import MarkdownFormField


from .fields import SpaceSeparatedTagsField
from .models import Problem, Review
    

class ProblemForm(forms.ModelForm):
    '''
    태그 help_text 한 곳에서 관리하기
    '''
    tags = SpaceSeparatedTagsField(
        required=False,
        help_text = '태그를 입력하세요. 공백문자로 태그를 구분하며 대소문자를 구분하지 않습니다.',
    )
    class Meta:
        model = Problem
        fields = (
            'title',
            'url',
            'tags',
            'description',
        )


class ReviewForm(forms.ModelForm):
    tags = SpaceSeparatedTagsField(
        required=False,
        help_text = '태그를 입력하세요. 공백문자로 태그를 구분하며 대소문자를 구분하지 않습니다.',
    )
    content = MarkdownFormField(
        label='내용',
        widget=MarkdownEditorWidget(),
    )
    class Meta:
        model = Review
        fields = (
            'tags',
            'content',
        )
