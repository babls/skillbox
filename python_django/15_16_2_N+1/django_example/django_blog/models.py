from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.CharField(max_length=400, verbose_name='текст поста')
    is_publihed = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author_post = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title
