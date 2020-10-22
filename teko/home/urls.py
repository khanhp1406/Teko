from . import views
from django.urls import path, include
from .views import HomeView,TopSeller

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('top-seller/', TopSeller.as_view(), name='top-seller'),
    path('books/', include('book.urls')),
]