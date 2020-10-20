from rest_framework import serializers
from book.models import Book, Author

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =['name', 'book']

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'cost']