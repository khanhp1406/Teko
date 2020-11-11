from django.http import HttpResponse
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
    template_name = 'book/search_results.html'
    paginate_by = 30

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Book.objects.filter(name__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, **kwargs)