from django import forms
from .models import NewsArticle

class NewsSubmissionForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'source_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'source_url': forms.URLInput(attrs={'class': 'form-control'}),
        }