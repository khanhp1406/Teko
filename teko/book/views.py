from django.shortcuts import render
from django.views import View
from .models import Book


# Create your views here.

class BookListView(View):
    def get(self, request, *args, **kwargs):
        Data = {'Books': Book.objects.all()}
        return render(request, 'book/listbook.html', context=Data)
