from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Заголовок объявления')
    description = models.TextField(max_length=1500,null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)  # auto_now_add Дата создания экземпляра атрибута
    updated_at = models.DateTimeField(auto_now = True)      # auto_now Дата обновления экземпляра атрибута
    price = models.FloatField(verbose_name='Цена', default=0)
    autor = models.ForeignKey('Autor', default=None, on_delete=models.CASCADE,related_name='Autor', verbose_name='Автор объявления')
    category = models.ForeignKey('Category', default=None, on_delete=models.CASCADE,related_name='Category', verbose_name='Рубрика объявления')
    type = models.ForeignKey('Type', default=None, null=True, on_delete=models.CASCADE,related_name='Type', verbose_name='Тип объявления')
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'     # Название таблицы Псевдоним
        ordering = ['title']            # Сортировка

class Autor(models.Model):
    name_autor = models.CharField(max_length=150, db_index=True)
    email_autor = models.CharField(max_length=150)
    number_mobile_autor = models.CharField(max_length=150)

    def __str__(self):
        return self.name_autor

    class Meta:
        ordering = ['name_autor']    # Сортировка

class Category(models.Model):
    name_category = models.CharField(max_length=150)

    def __str__(self):
        return self.name_category

class Type(models.Model):
    name_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name_type