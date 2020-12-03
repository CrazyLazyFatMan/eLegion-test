from django.db import models


class Author(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    name = models.CharField(verbose_name='Name', null=False, max_length=100)
    surname = models.CharField(verbose_name='Surname', null=False, max_length=100)

    def __str__(self):
        self.full_name = f'{self.name} {self.surname}'
        return self.full_name


class Book(models.Model):
    id = models.AutoField(null=False, primary_key=True)
    title = models.CharField(verbose_name='Title', null=False, max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
