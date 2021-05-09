from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, TextArea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholed': 'Name news'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholed': 'Anons'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholed': 'Publication date'
            }),
            "full_text": TextArea(attrs={
                'class': 'form-control',
                'placeholed': 'Text'
            }),
        }