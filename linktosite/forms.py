from django import forms

from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['category', 'title', 'link', 'image']
        labels = {
            'category': 'Категория:',
            'title': 'Имя ресурса:',
            'link': 'Ссылка на ресурс:',
            'image': 'Иконка:'
        }
