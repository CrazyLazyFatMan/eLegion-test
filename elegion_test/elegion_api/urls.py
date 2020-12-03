from .views import AuthorView, BookView, LibraryView
from rest_framework.routers import DefaultRouter

app_name = 'elegion_api'

router = DefaultRouter()
router.register(r'authors', AuthorView, basename='author')
router.register(r'books', BookView, basename='book')
router.register(r'library', LibraryView, basename='library')

