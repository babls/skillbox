from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=12, blank=True)
    about_myself = models.CharField(max_length=300, blank=True)
    #employee = forms.ModelChoiceField(queryset=Employee.objects.all())

    def __str__(self):
        return f'{self.user}'


