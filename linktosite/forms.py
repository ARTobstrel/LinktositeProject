from django import forms

from .models import Link


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ('category', 'title', 'link', 'image')
        labels = {
            'category': 'Категория:',
            'title': 'Имя ресурса:',
            'link': 'Ссылка на ресурс:',
            'image': 'Иконка:'
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form_field__category'}),
            'title': forms.TextInput(attrs={'class': 'form_field__title'}),
            'link': forms.TextInput(attrs={'class': 'form_field__link'}),
            'image': forms.FileInput(attrs={'class': 'form_field__image'}),
        }
