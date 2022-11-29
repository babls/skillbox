from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    TYPE_CHOICES = (
        ('Н', 'Начальный'),
        ('С', 'Средний'),
        ('В', 'Высокий')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    balance = models.FloatField(blank=True, verbose_name='Balance')
    balanceShopping = models.FloatField(blank=True, verbose_name='Balance shopping')
    status = models.CharField(max_length=1, choices=TYPE_CHOICES, default='Н')

    # employee = forms.ModelChoiceField(queryset=Employee.objects.all())

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profile'


class Shop(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Name shop')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Shops'
        verbose_name = 'Shop'


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Name product')
    price = models.FloatField(blank=True, verbose_name='Price')
    category = models.CharField(max_length=50, blank=True, verbose_name='Category')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'


class ListProductShop(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Shop')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Product')
    amount = models.IntegerField(blank=True, verbose_name='Amount')

    def __str__(self):
        return f'{self.shop, self.product}'

    class Meta:
        verbose_name_plural = 'List Products Shops'
        verbose_name = 'List Product Shop'


class History_shopping(models.Model):

    BUY_STATUS = (
        ('A', 'В корзине'),
        ('P', 'Оплачено'),
        ('C', 'Отмена')
    )

    date_of_shopping = models.DateField(auto_now_add=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Product')
    count = models.IntegerField(blank=True, verbose_name='Count')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Shop')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='User')
    status = models.CharField(max_length=1, choices=BUY_STATUS, default='A', verbose_name='Buy status')

    def __str__(self):
        return f'{self.user, self.shop, self.product}'

    class Meta:
        verbose_name_plural = 'History shopping'
        verbose_name = 'History shopping'
