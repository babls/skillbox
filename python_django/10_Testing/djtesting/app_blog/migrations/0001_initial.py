# Generated by Django 3.2.8 on 2022-05-05 09:43

import app_blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(max_length=1000, verbose_name='Содержание')),
                ('dataCreate', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('dateEdit', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата редактирования')),
                ('activity', models.BooleanField(blank=True, default=False, verbose_name='Флаг активности')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='FilesPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=app_blog.models.UploadToPathAndRename('E:\\Skillbox\\python_django-1\\python_django\\10_Testing\\djtesting\\files/upload\\here'), verbose_name='Изображение')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.blogpost', verbose_name='Пост к которому привязанно изображение')),
            ],
        ),
    ]
