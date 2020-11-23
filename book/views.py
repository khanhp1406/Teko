from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book, Bookdetail, UserClick, ContentSimilarityBook
from django.db.models import Q
from django.core.paginator import Paginator
from django.db import connections

from book.serializer import BookSerializer
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
                              ON (b.id_tiki = bd.id_tiki) ORDER BY bd.review_count DESC
                          """)
        queryset = dictfetchall(cursor)

        return queryset

def top_seller_book(request):
    
    context = {
        'best_seller': best_seller_items,
        'best_rating': best_rating_items
    }
    return render(request, "listbook_top_seller.html", context)


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
        if self.request.user.is_authenticated:
            user_click = UserClick(
                user_id = self.request.user.id,
                book_id = context['object'].id
            )
            user_click.save()
        return context

class RecommendBookBySimilarityView(APIView):
    def get(self, request):
        id_tiki = request.GET.get('id_tiki')
        id_by_title = ContentSimilarityBook.objects.get(id_tiki=id_tiki).get_title_similarity()
        id_by_des = ContentSimilarityBook.objects.get(id_tiki=id_tiki).get_descript_similarity()
        rs_title_books = Book.objects.filter(id_tiki__in=id_by_title)
        rs_des_books = Book.objects.filter(id_tiki__in=id_by_des)

        rs_title_books_data = []
        for book in rs_title_books:
            data = BookSerializer(book).data
            rs_title_books_data.append(data)

        rs_des_books_data = []
        for book in rs_des_books:
            data = BookSerializer(book).data
            rs_des_books_data.append(data)
        return Response({'rs_by_title': rs_title_books_data, 'rs_by_des': rs_des_books_data})


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict."
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
