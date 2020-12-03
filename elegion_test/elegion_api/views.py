from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, LibrarySerializer
from .viewsets import GetViewSet


class AuthorView(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class LibraryPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'


class LibraryView(GetViewSet):
    queryset = Book.objects.all().select_related(
        'author'
    )

    serializer_class = LibrarySerializer

    pagination_class = LibraryPagination

    filter_backends = (
        SearchFilter,
    )

    search_fields = (
        'title',
        'author__name',
        'author__surname',
    )


