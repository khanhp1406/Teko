from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'book/listbook.html'
    context_object_name = 'Books'
    paginate_by = 30

class SearchBookView(ListView):
    model = Book
    template_name = 'book/listbook.html'

    def search(self):
        query = self.request.GET.get('q')
        result = Book.objects.filter(Q(name__icontains=query) | Q(short_description__icontains=query))
        return result