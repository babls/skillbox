'''
from django.dispatch import receiver
from django.db.models.signals import post_save
from app_news.models import News
from app_users.models import Profile


@receiver(post_save, sender=News)
def update_published_news_count(**kwargs):
    print('hello = ' + str(News.author))
    user = Profile.objects.filter(user=News.author)
    user.published_news_count += 1
    user.save()
    print('save')
'''

# Пытался через signals реализовать подсчет количество новостей у пользователя

