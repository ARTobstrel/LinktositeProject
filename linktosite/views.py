from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from linktosite.forms import LinkForm
from linktosite.models import Category, Link


def main_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'main.html', context)

def new_link_view(request):
    if request.method != 'POST':
        form = LinkForm()
    else:
        form = LinkForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_view'))

    context = {'form': form}
    return render(request, 'new_link.html', context)