from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    GROUP_USER_CHOICES = (
        ('N', 'Normal'),
        ('V', 'Verified'),
        ('M', 'Moderator')
    )

    VERIFICATION_USER_CHOICES = (
        ('S', 'Верификация отсутствует'),
        ('R', 'Запрос на верификацию'),
        ('V', 'Верификация успешно пройдена'),
        ('N', 'Верификация отклонена')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=12, blank=True)
    verification = models.CharField(max_length=2, choices=VERIFICATION_USER_CHOICES, default='S')
    published_news_count = models.IntegerField(default=0)
    Group_user = models.CharField(max_length=2, choices=GROUP_USER_CHOICES, default=('N', 'Normal'))

    def __str__(self):
        return f'{self.Group_user}, {self.published_news_count}'
