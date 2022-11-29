from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name=_('name shop'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = _('shops')
        verbose_name = _('shop')


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name=_('name product'))
    price = models.FloatField(blank=True, verbose_name=_('price'))
    category = models.CharField(max_length=50, blank=True, verbose_name=_('category'))
    shop = models.ManyToManyField(Shop)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = _('products')
        verbose_name = _('product')


class Action_and_offer(models.Model):
    TYPE_CHOICES = (
        ('А', 'Акция'),
        ('П', 'Предложение')
    )

    name = models.CharField(max_length=50, blank=True, verbose_name=_('name action'))
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='А')
    text_action = models.CharField(max_length=200, blank=True, verbose_name=_('text'))
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('shop'))

    def __str__(self):
        return f'{self.name, self.shop, self.type, self.text_action}'

    class Meta:
        verbose_name_plural = _('actions and offers')
        verbose_name = _('action and offer')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    balance = models.FloatField(blank=True, verbose_name=_('balance'))
    telephone_number = models.CharField(max_length=12, blank=True, verbose_name=_('telephone_number'))
    city = models.CharField(max_length=50, blank=True, verbose_name=_('city'))
    about_myself = models.CharField(max_length=300, blank=True, verbose_name=_('about_myself'))

    # employee = forms.ModelChoiceField(queryset=Employee.objects.all())

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')


class History_shopping(models.Model):
    date_of_shopping = models.DateField(null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('shop'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('product'))
    count = models.IntegerField(blank=True, verbose_name=_('count'))
    total = models.FloatField(blank=True, verbose_name=_('total'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('user'))

    def __str__(self):
        return f'{self.user, self.shop, self.product}'

    class Meta:
        verbose_name_plural = _('history shopping')
        verbose_name = _('history shopping')
