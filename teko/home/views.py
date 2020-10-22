from django.shortcuts import render
from django.views import View


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'pages/index.html')

class TopSeller(View):
    def get(self, request):
        return render(request, 'pages/top-seller.html')

