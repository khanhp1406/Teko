from django.shortcuts import render
from book.models import Book
# Create your views here.
def listView(request):
    Data = {'Books':Book.objects.all()}
    return render(request, 'book/listbook.html', Data)