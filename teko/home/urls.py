from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('book/', include('book.urls')),
]