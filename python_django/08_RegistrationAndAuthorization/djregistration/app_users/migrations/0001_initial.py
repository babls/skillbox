# Generated by Django 3.2.11 on 2022-04-14 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=36)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=12)),
                ('verification', models.CharField(choices=[('S', 'Верификация отсутствует'), ('R', 'Запрос на верификацию'), ('V', 'Верификация успешно пройдена'), ('N', 'Верификация отклонена')], default='S', max_length=2)),
                ('published_news_count', models.IntegerField(default=0)),
                ('Group_user', models.CharField(choices=[('N', 'Normal'), ('V', 'Verified'), ('M', 'Moderator')], default=('N', 'Normal'), max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]