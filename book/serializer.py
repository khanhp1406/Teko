from rest_framework import serializers
from book.models import Book, Bookdetail

class BookSerializer(serializers.ModelSerializer):
	author = serializers.SerializerMethodField('get_author')
	def get_author(self, obj):
		return Bookdetail.objects.get(pk=obj.pk).author
	class Meta:
		model = Book
		fields = ('id', 'id_tiki', 'name', 'category', 'short_description', 'price', 'discount', 'thumnail', 'author')