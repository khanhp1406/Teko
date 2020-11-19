from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Bookdetail, UserClick
from django.db.models import Q
from django.core.paginator import Paginator
from django.db import connections

# Create your views here.

class BookListView(ListView):
    
    template_name = 'book/listbook.html'
    context_object_name = 'Books'
    paginate_by = 30

    def get_queryset(self):
        cursor = connections["default"].cursor()
        cursor.execute("""SELECT *
                          FROM book as b
                          INNER JOIN bookdetail as bd
                              ON (b.id_tiki = bd.id_tiki)
                          """)
        queryset = dictfetchall(cursor)

        return queryset

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

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        
        context = super(BookDetailView, self).get_context_data()
        user_click = UserClick(
            user_id = self.request.user.id,
            book_id = context['object'].id_tiki
        )
       # user_click.save()
        return context



def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict."
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
