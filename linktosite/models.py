from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


def image_folder(instance, filename):
    """Эта функция автоматически переименовывает файл с картинкой и сохраняет его в папку с аналогичным названием"""
    filename = '{0}.{1}'.format(instance.slug, filename.split('.')[1])
    return '{0}/{1}'.format(instance.slug, filename)


class Link(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    slug = models.SlugField(blank=True)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return self.title
