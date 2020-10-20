from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from book.api.serializers import BookSerializers
from book.models import Book
@api_view(['GET',])
def api_detail_blog_view(request, slug):
    try:
        book_post = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializers(book_post) 
        return Response(serializer.data)