from django.db import models
from django.db.models.signals import pre_save
from pytils.translit import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField(max_length=25)
    slug = models.SlugField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


def pre_save_category_slug(sender, instance, *args, **kwargs):
    instance.name = instance.name.title()

    """Эта функция автоматически генерирует slug нашего создаваемого объеката, если он отсутствует"""
    if not instance.slug:
        slug = slugify(instance.name)
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)


def image_folder(instance, filename):
    """Эта функция автоматически переименовывает файл с картинкой и сохраняет его в папку с аналогичным названием"""
    filename = '{0}.{1}'.format(instance.slug, filename.split('.')[1])
    return '{0}/{1}'.format(instance.slug, filename)


class Link(models.Model):
    """Модель ссыллок. Каждая ссылка имеет свою категорию"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('Name', max_length=25)
    slug = models.SlugField(blank=True)
    link = models.CharField(max_length=100)
    image = models.ImageField('Image url', blank=True, upload_to=image_folder)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"


def pre_save_link_slug(sender, instance, *args, **kwargs):
    """Эта функция автоматически генерирует slug нашего создаваемого объеката, если он отсутствует"""
    if not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug


pre_save.connect(pre_save_link_slug, sender=Link)


class UnauthorizedUserLink(models.Model):
    title = models.CharField('Name', max_length=25)
    slug = models.SlugField(blank=True)
    link = models.CharField(max_length=100)
    image = models.ImageField('Image url', blank=True, upload_to=image_folder)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "UnauthorizedUserLink"
        verbose_name_plural = "UnauthorizedUserLinks"


def pre_save_Unlink_slug(sender, instance, *args, **kwargs):
    """Эта функция автоматически генерирует slug нашего создаваемого объеката, если он отсутствует"""
    if not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug


pre_save.connect(pre_save_Unlink_slug, sender=UnauthorizedUserLink)
