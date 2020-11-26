import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from book.serializer import BookSerializer
from .models import Book, Bookdetail, UserClick, ContentSimilarityBook, CollabFilteringRsBook
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
                              ON (b.id_tiki = bd.id_tiki) ORDER BY bd.review_count DESC
                          """)
        queryset = dictfetchall(cursor)

        return queryset

class BestSellerBookView(ListView):
    template_name = 'pages/home.html'
    context_object_name = 'Books'
    
    def get_queryset(self):
        cursor = connections["default"].cursor()
        cursor.execute("""SELECT *
                          FROM book as b
                          INNER JOIN bookdetail as bd
                              ON (b.id_tiki = bd.id_tiki) ORDER BY bd.review_count DESC LIMIT 9
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

        # rs_title_books_data = []
        rs_books = []
        for book in rs_title_books:
            data = BookSerializer(book).data
            rs_books.append(data)

        rs_des_books_data = []
        for book in rs_des_books:
            data = BookSerializer(book).data
            rs_books.append(data)
        # return Response({'rs_by_title': rs_title_books_data, 'rs_by_des': rs_des_books_data})
        return Response({'rs': rs_books})



class RecommendBookByKnnView(APIView):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            rs_knn_books = Book.objects.all().order_by('?')[:9]
        else:
            user_click = UserClick.objects.filter(user_id=user.id)
            history_id = []
            for uc in user_click:
                    history_id.append(Book.objects.get(pk=uc.book_id).id_tiki)

            if not history_id:
                rs_knn_books = Book.objects.all().order_by('?')[:9]
            else:
                rs_ids = []
                for id_ in history_id:
                    try:
                        rs_ids.extend(CollabFilteringRsBook.objects.get(id_tiki=id_).get_rs1())
                    except:
                        pass
                rs_knn_books = Book.objects.filter(id_tiki__in=rs_ids)
            # return Response({'data': rs_ids})

        rs_books = []
        for book in rs_knn_books:
            data = BookSerializer(book).data
            rs_books.append(data)
        if len(rs_books)>12:
            rs_books = random.sample(rs_books, 12)
        return Response({'rs': rs_books})

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict."
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
