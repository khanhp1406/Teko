from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
from book.models import Book

def autocomplete(request):
    if 'term' in request.GET:

        qs = Book.objects.filter(name__icontains=request.GET.get('term'))
        books = list()
        for product in qs:
            books.append(product.name)
        # titles = [product.title for product in qs]
        return JsonResponse(books, safe=False)
    return render(request, 'pages/home.html')


class HomeView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/home.html')


class LoginView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/login.html')
