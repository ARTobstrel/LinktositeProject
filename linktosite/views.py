from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View

from linktosite.forms import LinkForm, CategoryForm
from linktosite.models import Category, UnauthorizedUserLink


class MainView(ListView):
    model = Category
    template_name = 'linktosite/main.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Category.objects.filter(owner=self.request.user)
            return queryset

# Нужно что то здесь поменят чтобы выводило линки неавторизованного пользователя
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['un_link'] = UnauthorizedUserLink.objects.all()

        return context


class New_link_view(View):
    new_link_template = 'linktosite/new_link.html'

    def get(self, request):
        form = LinkForm(request.user.id)
        context = {'form': form}
        return render(request, 'linktosite/new_link.html', context)

    def post(self, request):
        form = LinkForm(request.user.id, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_view'))

        return render(request, 'linktosite/new_link.html', {'form': form})


class New_category_view(View):

    def get(self, request):
        form = CategoryForm()
        context = {'form': form}
        return render(request, 'linktosite/new_category.html', context)

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return HttpResponseRedirect(reverse('new_link_view'))

        return render(request, 'linktosite/new_category.html', {'form': form})
