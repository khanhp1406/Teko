from . import views
from django.urls import path, include
from .views import HomeView, LoginView, autocomplete
from book.views import BookListView
from book.api.views import BookList
from book.api.views import BookDetailAPI

urlpatterns = [
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('', HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('listbook/', BookListView.as_view(), name ='Books'),
    path('api-book/', BookList.as_view()),
    path('api-book/<int:pk>', BookDetailAPI.as_view(), name = "Bookdetail"),
    path('accounts/', include('allauth.urls')),

]