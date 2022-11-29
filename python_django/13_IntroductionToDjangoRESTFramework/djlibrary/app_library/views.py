from app_library.models import Book, Author
from app_library.serializers import BooksSerializer, AuthorsSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = BooksSerializer


    def get_queryset(self):
        queryset = Book.objects.all()
        # Получаем набор всех записей из таблицы Book
        book_name = self.request.query_params.get('name')
        book_author = self.request.query_params.get('author')
        book_page = self.request.query_params.get('page')
        if book_page:
            if book_page.find(">") != -1:
                book_page = book_page.replace(">", '')
                queryset = queryset.filter(page_count__gt=int(book_page))
                print('>')
            elif book_page.find("<") != -1:
                book_page = book_page.replace("<", '')
                book_page = int(book_page)
                queryset = queryset.filter(page_count__lt=book_page)
                print('<')
            else:
                queryset = queryset.filter(page_count=book_page)

        if book_name:
            queryset = queryset.filter(name=book_name)
        if book_author:
            author = Author.objects.get(name=book_author)
            queryset = queryset.filter(author=author.id)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = AuthorsSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        author_name = self.request.query_params.get('name')

        if author_name:
            queryset = queryset.filter(name=author_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
