import random

import lorem
from app_house.models import House, News, TypeHouse, CountRooms
from django.core.management import BaseCommand
from django.utils.timezone import now


class Command(BaseCommand):
    help = 'Добавить 100 объявлений и 10 новостей'

    def handle(self, *args, **options):
        for h in range(0, 100):
            id_typeHouse = random.randint(1, 2)
            id_countRooms = random.randint(1, 7)
            id_adress = random.randint(1, 100)
            tmp_house = House.objects.create(
                Name=f'Жильё {h}',
                Address=f'Улица пример №{id_adress}',
                Price=int(h) * 1000000,
                TypeHouse=TypeHouse.objects.get(id=id_typeHouse),
                CountRooms=CountRooms.objects.get(id=id_countRooms)
            )

            News.objects.create(
                Name=f'Новость {h} Добавлено новое объявление о продаже квартиры',
                House=tmp_house,
                is_published=True,
                description=lorem.paragraph(),
                published_at=now()
            )

        self.stdout.write('Объявления и новости успешно загружены в БД!')
