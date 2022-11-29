from django.db import models
from django.urls import reverse


class TypeHouse(models.Model):
    Name = models.CharField(max_length=100, blank=True, verbose_name='Type house')

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name_plural = 'Типы помещений'
        verbose_name = 'Тип помещения'


class CountRooms(models.Model):
    Name = models.CharField(max_length=100, blank=True, verbose_name='Count rooms')

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name_plural = 'Количество комнат'
        verbose_name = 'Количество комнат'


class House(models.Model):
    Name = models.CharField(max_length=100, blank=True, verbose_name='Name house')
    Address = models.CharField(max_length=100, blank=True, verbose_name='Address house')
    Price = models.FloatField(blank=True, verbose_name='Price')
    TypeHouse = models.ForeignKey(TypeHouse, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Type house')
    CountRooms = models.ForeignKey(CountRooms, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Count rooms')

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name_plural = 'Жильё'
        verbose_name = 'Жильё'


class News(models.Model):
    Name = models.CharField(max_length=100, blank=True, verbose_name='Name news')
    House = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True, verbose_name='House')
    is_published = models.BooleanField(default=False)
    description = models.TextField(default='', verbose_name='Описание')
    published_at = models.DateTimeField(null=True, verbose_name='Дата публикации')

    def get_absolute_url(self):
        return reverse('news-item', args=[str(self.id)])

    def __str__(self):
        return f'{self.Name}'

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
