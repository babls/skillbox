from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


class News(models.Model):

    VERIFICATION_NEWS_CHOICES = (
        ('R', 'Запрос на публикацию отправлен'),
        ('V', 'Опубликована'),
        ('N', 'Отклонено')
    )

    name = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(max_length=1000, verbose_name='Содержание')
    dataCreate = models.DateTimeField(default=now, blank=True, verbose_name='Дата создания')
    dateEdit = models.DateTimeField(default=now, blank=True, verbose_name='Дата редактирования')
    moderate = models.CharField(max_length=2, choices=VERIFICATION_NEWS_CHOICES, default='R', blank=True)
    activity = models.BooleanField(default=False, verbose_name='Флаг активности', blank=True)
    tag = models.CharField(default='Новость', max_length=50, verbose_name='Тэг', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')

    def __str__(self):
        return f'{self.id}'
        #return f'{self.name}, {self.dataCreate}, {self.activity}'


class Comment(models.Model):
    nameUser = models.CharField(max_length=50, verbose_name='Имя пользователя', blank=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, related_name='User_comment', verbose_name='Пользователь', blank=True)
    text = models.TextField(max_length=400, verbose_name='Текст комментария')
    id_news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE, related_name='Comment', verbose_name='Комментарий')

    def __str__(self):
        return f'{self.nameUser}, {self.text[0:16]+"..."}'
