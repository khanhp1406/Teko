from django.urls import path
from . import views
from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='listbook'),
]
