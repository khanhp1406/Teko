from . import views
from django.urls import path, include
from .views import HomeView, LoginView, autocomplete
from book.views import BookListView
from book.api.views import BookList
from book.api.views import BookDetailAPI
from django.contrib.auth import views as auth_views
from book.views import SearchBookView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name ='logout'),
    path('listbook/', BookListView.as_view(), name ='Books'),
    path('search/', SearchBookView.as_view(), name='search_books'),
    path('api-book/', BookList.as_view()),
    path('api-book/<int:pk>', BookDetailAPI.as_view(), name = "Bookdetail"),
    path('accounts/', include('allauth.urls')),
]