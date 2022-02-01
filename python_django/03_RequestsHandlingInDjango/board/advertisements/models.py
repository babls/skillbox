from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True)
    description = models.TextField
    created_at = models.DateTimeField(auto_now_add = True, db_index=True)  # auto_now_add Дата создания экземпляра атрибута
    updated_at = models.DateTimeField(auto_now = True)      # auto_now Дата обновления экземпляра атрибута
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,related_name='adStatus')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,related_name='adType')
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'     # Название таблицы Псевдоним
        ordering = ['title']    # Сортировка

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)
