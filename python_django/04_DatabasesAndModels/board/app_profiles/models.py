from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    birthday = models.DateField()

class Advertisement(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField(verbose_name='Цена', default=10)
