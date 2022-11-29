# Generated by Django 3.1.7 on 2022-02-22 16:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(max_length=1000, verbose_name='Содержание')),
                ('dataCreate', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('dateEdit', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата редактирования')),
                ('activity', models.BooleanField(default=False, verbose_name='Флаг активности')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameUser', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('text', models.TextField(max_length=400, verbose_name='Текст комментария')),
                ('id_news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to='app_news.news', verbose_name='Комментарий')),
            ],
        ),
    ]
