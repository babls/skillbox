from app_library.models import Book, Author
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Добавить 100 книг'

    def handle(self, *args, **options):
        for i in range(1, 101):
            Book.objects.create(
                name=f'Название книги {i}',
                isbn='ISBN 978-3-16-148410-0',
                year_of_issue='2020-01-01',
                page_count=i,
                author=Author.objects.get(id=i))
        self.stdout.write('Книги успешно загруженны')
