from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View

from linktosite.forms import LinkForm
from linktosite.models import Category


class MainView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'main.html'


class New_link_view(View):
    def get(self, request):
        form = LinkForm()
        context = {'form': form}
        return render(request, 'new_link.html', context)

    def post(self, request):
        form = LinkForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_view'))

        return render(request, 'new_link.html', {'form': form})
