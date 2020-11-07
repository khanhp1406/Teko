from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
from book.models import Book


def autocomplete(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = Book.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist , safe=False)

class HomeView(View):
    def get(self, request):
        return render(request, 'pages/home.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'pages/login.html')
