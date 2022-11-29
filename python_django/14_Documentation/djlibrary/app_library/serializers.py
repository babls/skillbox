from app_library.models import Book, Author
from rest_framework import serializers


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True, source='author.name')

    class Meta:
        model = Book
        fields = "__all__"


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'date_of_birth']
