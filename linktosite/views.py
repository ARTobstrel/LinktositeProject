from django.shortcuts import render
from linktosite.models import Category, Link


def main_view(request):
    categories = Category.objects.all()
    links = Link.objects.all()
    context = {
        'categories': categories,
        'links': links
    }

    return render(request, 'main.html', context)