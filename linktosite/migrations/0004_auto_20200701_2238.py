# Generated by Django 3.0.6 on 2020-07-01 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import linktosite.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linktosite', '0003_auto_20200428_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='image',
            field=models.ImageField(blank=True, upload_to=linktosite.models.image_folder, verbose_name='Image url'),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Name'),
        ),
    ]