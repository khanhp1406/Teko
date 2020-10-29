from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
# Create your views here.

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'book/listbook.html'
    context_object_name = 'Books'
    paginate_by = 30