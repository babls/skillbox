from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = _('user'))
    city = models.CharField(max_length=36, blank=True, verbose_name = _('city'))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name = _('date_of_birth'))
    telephone_number = models.CharField(max_length=12, blank=True, verbose_name = _('telephone_number'))
    about_myself = models.CharField(max_length=300, blank=True, verbose_name = _('about_myself'))
    #employee = forms.ModelChoiceField(queryset=Employee.objects.all())

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')


