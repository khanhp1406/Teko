from django.db import models
# Create your models here.

class Puplisher(models.Model):
    name  = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', through='Authored')

class Book(models.Model):
    name = models.CharField(max_length=150)
    authors = models.ManyToManyField('Author', through='Authored')
    publisher = models.ForeignKey(Puplisher, on_delete=models.CASCADE)
    cost = models.IntegerField()

class Authored(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Comment(models.Model):
    tilte = models.CharField(max_length=100)
