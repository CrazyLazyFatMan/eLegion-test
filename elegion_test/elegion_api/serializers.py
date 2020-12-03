from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name')
    author_surname = serializers.CharField(source='author.surname')
    book_id = serializers.IntegerField(source='id')
    book_title = serializers.CharField(source='title')

    class Meta:
        model = Book
        fields = (
            'book_id',
            'book_title',
            'author_name',
            'author_surname',
        )