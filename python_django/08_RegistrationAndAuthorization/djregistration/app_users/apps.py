from django.apps import AppConfig
from app_users import *


class AppUsersConfig(AppConfig):
    name = 'app_users'

    #def ready(self):
    #    import app_users.signals
