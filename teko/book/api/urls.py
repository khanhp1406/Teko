from django.urls import path
from book.api.views import api_detail_blog_view

app_name = 'book'

urlpatterns = [
    path('<slug>/', api_detail_blog_view, name = 'detail'),
]
