from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        label='리뷰 작성',
        max_length='140'
    )
    score = forms.IntegerField(max_value=10, min_value=0)

    class Meta:
        model = Review
        fields = ('content', 'score',)