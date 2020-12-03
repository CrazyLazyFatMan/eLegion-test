from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class CreateAuthorTest(APITestCase):

    def setUp(self):
        self.author = {'name': 'John', 'surname': 'Ringo'}

    def test_create_author(self):
        response = self.client.post('/api/authors/', self.author)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CreateBookTest(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name='First',
            surname='Stranger'
        )
        self.book = {'title': 'How to insist', 'author': self.author.id}

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateAuthorTest(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name='Shaquille',
            surname='Jordan'
        )
        self.data = AuthorSerializer(self.author).data
        self.data.update({'surname': 'O`Neal'})

    def test_update_author(self):
        response = self.client.put(f'/api/authors/{self.author.id}/', data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateBookTest(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name='Adolf',
            surname='Dassler'
        )
        self.book = Book.objects.create(
            title='Catch and throw',
            author=self.author
        )
        self.data = BookSerializer(self.book).data
        self.data.update({'title': 'Why "Puma" sucks?'})

    def test_update_book(self):
        response = self.client.put(f'/api/books/{self.book.id}/', data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAuthor(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name='Robert',
            surname='Weide'
        )

    def test_get_author(self):
        response = self.client.get(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetBook(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name='Robert',
            surname='Weide'
        )
        self.book = Book.objects.create(
            title='Resist memes addiction',
            author=self.author
        )

    def test_get_author(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllAuthorsTest(APITestCase):

    def setUp(self):
        Author.objects.create(
            name='Fedor',
            surname='Konyukhov'
        )
        Author.objects.create(
            name='Frank',
            surname='Sinatra'
        )
        Author.objects.create(
            name='Ivan',
            surname='Susanin'
        )

    def test_get_authors(self):
        response = self.client.get('/api/authors/')
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllBooksTest(APITestCase):

    def setUp(self):
        self.authors = [
            Author.objects.create(
                name='Fedor',
                surname='Konyukhov'
            ),
            Author.objects.create(
                name='Frank',
                surname='Sinatra'
            ),
            Author.objects.create(
                name='Ivan',
                surname='Susanin'
            )
        ]

        Book.objects.create(
            title='How to stay at home',
            author=self.authors[0]
        )
        Book.objects.create(
            title='How to find your way',
            author=self.authors[1]
        )
        Book.objects.create(
            title='Where swamps locates',
            author=self.authors[2]
        )

    def test_get_books(self):
        response = self.client.get('/api/books/')
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
