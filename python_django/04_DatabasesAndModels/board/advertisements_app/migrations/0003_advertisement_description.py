# Generated by Django 4.0 on 2021-12-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0002_alter_advertisement_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='description',
            field=models.TextField(max_length=1500, null=True, verbose_name='Описание'),
        ),
    ]