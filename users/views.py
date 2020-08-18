from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate

from users.forms import MyUserCreationForm


def register(request):
    """Registration new user"""
    if request.method != 'POST':
        form = MyUserCreationForm()
    else:
        form = MyUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('main_view'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
