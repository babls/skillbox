# Generated by Django 3.2.15 on 2022-08-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_house', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countrooms',
            options={'verbose_name': 'Количество комнат', 'verbose_name_plural': 'Количество комнат'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'Жильё', 'verbose_name_plural': 'Жильё'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='typehouse',
            options={'verbose_name': 'Тип помещения', 'verbose_name_plural': 'Типы помещений'},
        ),
        migrations.AddField(
            model_name='news',
            name='descriprion',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='published_at',
            field=models.DateTimeField(null=True, verbose_name='Дата публикации'),
        ),
    ]
