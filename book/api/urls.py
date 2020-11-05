from django.urls import path, include
from .views import BookList

urlpattens = [
    path('', BookList.as_view(), name = 'get')
]