import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View

from linktosite.forms import LinkForm, CategoryForm, UpdateLinkForm
from linktosite.models import Category, Link, UnauthorizedUserLink

logger = logging.getLogger('django')


class MainView(ListView):
    """Вывод всех линков. Главный экран"""

    model = Category
    template_name: str = 'linktosite/main.html'
    logger.info('Its working')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Category.objects.filter(owner=self.request.user)

            return queryset.order_by('id')

    def get_context_data(self, **kwargs) -> dict:
        context: dict = super().get_context_data(**kwargs)
        context['un_link'] = UnauthorizedUserLink.objects.all()
        return context


class NewLinkView(View):
    """Создание новой линки"""

    template_name: str = 'linktosite/new_link.html'

    def get(self, request):
        form = LinkForm(request.user.id)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = LinkForm(request.user.id, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_view'))
        return render(request, self.template_name, {'form': form})


class NewCategoryView(View):
    """Создание новой категории"""
    tempate_name: str = 'linktosite/new_category.html'

    def get(self, request):
        form = CategoryForm()
        context = {'form': form}
        return render(request, self.tempate_name, context)

    def post(self, request):
        form = CategoryForm(request.POST)
        next = request.POST.get('next', '/')
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return HttpResponseRedirect(next)

        return render(request, self.tempate_name, {'form': form})


class EditLinkView(View):
    """Редактирование линков, в том числе удаление"""

    def get(self, request, id):
        category = Category.objects.get(id=id)
        context: dict = {'category': category}
        return render(request, 'linktosite/edit_links.html', context)


@login_required
def delete_link(request, id: int):
    """Удаление линков"""

    try:
        link = Link.objects.get(id=id)
        category_id = link.category.id
        link.delete()
        return HttpResponseRedirect(reverse('edit_link_view', args=(category_id,)))
    except link.DoesNotExist:
        return HttpResponseRedirect("/")


class UpdateLinkView(View):
    """Редактирование линки. Редактировать можно всё кроме изображения"""

    template_name: str = 'linktosite/update_link.html'

    def get(self, request, id):
        link = Link.objects.get(id=id)
        form = UpdateLinkForm(request.user.id, instance=link)
        context = {'form': form, 'link_id': id,
                   'category_id': link.category.id}
        return render(request, self.template_name, context)

    def post(self, request, id: int):
        link = Link.objects.get(id=id)
        category_id = link.category.id
        form = UpdateLinkForm(request.user.id, request.POST,
                              request.FILES, instance=link)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit_link_view', args=(category_id,)))
        return render(request, self.template_name, {'form': form, 'link_id': id})


@login_required
def delete_cat(request, id: int) -> HttpResponseRedirect:
    """Удаление категорий"""

    try:
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect("/")
    except category.DoesNotExist:
        return HttpResponseRedirect("/")


class RenameCatView(View):
    """Переименовывание категории"""

    template_name: str = 'linktosite/rename_category.html'

    def get(self, request, id: int) -> render:
        get_category = Category.objects.get(id=id)
        form = CategoryForm(instance=get_category)
        context = {'form': form, 'category_id': id}
        return render(request, self.template_name, context)

    def post(self, request, id: int):
        get_category = Category.objects.get(id=id)
        form = CategoryForm(request.POST, instance=get_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit_link_view', args=(get_category.id,)))
        return render(request, self.template_name, {'form': form, 'category_id': id})


class UserListView(ListView):
    """Вывод всех пользователей"""

    model = User
    context_object_name = 'users'
    template_name = 'users/user_list.html'
    ordering = 'id'


@login_required
def delete_user(request, id: int) -> HttpResponseRedirect:
    """Удаление пользователей"""

    if request.user.is_superuser:
        try:
            user = User.objects.get(id=id)
            user.delete()
            return HttpResponseRedirect(reverse('user_list'))
        except user.DoesNotExist:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
