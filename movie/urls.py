from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('movies/', home_view, name='landing_page'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
]
