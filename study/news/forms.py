from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholed': 'Name news'
            }),
            "anons": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholed': 'Anons'
            }),
            "date": forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholed': 'Publication date'
            }),
            "full_text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholed': 'Text'
            }),
        }