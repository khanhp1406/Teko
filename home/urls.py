from . import views
from django.urls import path, include
from .views import HomeView, LoginView, autocomplete
from book.views import BookListView, SearchBookView, BookDetailView
from book.api.views import BookList
from book.api.views import BookDetailAPI
from book.views import RecommendBookBySimilarityView
from django.contrib.auth import views as auth_views


from django.conf.urls import url


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name ='logout'),
    path('listbook/', BookListView.as_view(), name ='Books'),
    path(r'^search/$', SearchBookView.as_view(), name='search_books'),
    path('api-book/', BookList.as_view()),
    path('api-book/<int:pk>', BookDetailAPI.as_view(), name = "Bookdetail"),
    path('accounts/', include('social_django.urls', namespace = "social_django")),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('detail/rec_content/', RecommendBookBySimilarityView.as_view(), name='content_rs')
]