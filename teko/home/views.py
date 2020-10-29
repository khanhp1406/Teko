from django.shortcuts import render
from django.views import View


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'pages/home.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'pages/login.html')