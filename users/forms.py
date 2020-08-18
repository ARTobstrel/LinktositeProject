from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'password1')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form_field__name'}),
            'password1': forms.TextInput(attrs={'class': 'form_field__name'}),
            'password2': forms.TextInput(attrs={'class': 'form_field__name'}),
        }
