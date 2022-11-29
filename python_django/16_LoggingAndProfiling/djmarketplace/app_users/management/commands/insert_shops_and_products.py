from app_users.models import Shop, Product, ListProductShop
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Добавить 100 магазинов и товаров'

    def handle(self, *args, **options):
        for i in range(0, 100):
            tmp_shop = Shop.objects.create(name=f'Магазин {i}')
            tmp_product = Product.objects.create(
                name=f'Товар {i}',
                price=i,
                category='Test'
                )
            ListProductShop.objects.create(
                shop=tmp_shop,
                product=tmp_product,
                amount=i
            )
        self.stdout.write('Магазины и товары успешно загружены в БД!')
