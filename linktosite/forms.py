from django import forms

from .models import Link, Category


class LinkForm(forms.ModelForm):

    # Переписываем категорию, чтобы отражались те пункты которые принадлежат конкретному пользователю
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(
            owner=self.user)

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


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Название категории'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_field__title'}),
        }
