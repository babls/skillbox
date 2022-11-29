from app_library.models import Author
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Добавить 100 авторов'

    def handle(self, *args, **options):
        for i in range(0, 100):
            Author.objects.create(name=f'Автор Имя{i}', surname=f'Автор Фамилия{i}', date_of_birth='2000-01-01')
        self.stdout.write('Авторы успешно загружены')
