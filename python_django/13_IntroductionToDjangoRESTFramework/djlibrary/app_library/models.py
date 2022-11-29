from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name=_('Имя'))
    surname = models.CharField(max_length=50, blank=True, verbose_name=_('Фамилия'))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_('Дата рождения'))

    def __str__(self):
        return f'{self.name, self.surname}'

    class Meta:
        verbose_name_plural = _('Авторы')
        verbose_name = _('Автор')


class Book(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name=_('Имя'))
    isbn = models.CharField(max_length=50, blank=True, verbose_name=_('Международный стандартный книжный номер'))
    year_of_issue = models.DateField(null=True, blank=True, verbose_name=_('Год выпуска'))
    page_count = models.IntegerField(blank=True, verbose_name=_('Количество страниц'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Автор книги'))

    def __str__(self):
        return f'{self.name, self.isbn}'

    class Meta:
        verbose_name_plural = _('Книги')
        verbose_name = _('Книга')
