from django.utils.timezone import now
from django.db import models


class News(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(max_length=1000, verbose_name='Содержание')
    dataCreate = models.DateTimeField(default=now, blank=True, verbose_name='Дата создания')
    dateEdit = models.DateTimeField(default=now, blank=True, verbose_name='Дата редактирования')
    activity = models.BooleanField(default=False, verbose_name='Флаг активности')

    def __str__(self):
        return f'{self.id}'
        #return f'{self.name}, {self.dataCreate}, {self.activity}'


class Comment(models.Model):
    nameUser = models.CharField(max_length=50, verbose_name='Имя пользователя')
    text = models.TextField(max_length=400, verbose_name='Текст комментария')
    id_news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE, related_name='Comment', verbose_name='Комментарий')

    def __str__(self):
        return f'{self.nameUser}, {self.text[0:16]+"..."}'
