from app_store.models import Shop
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Добавить 1000 магазинов'

    def handle(self, *args, **options):
        for i in range(100, 1100):
            Shop.objects.create(name=f'Магазин {i}')

        self.stdout.write('Магазины успешно загружены')
