from django.urls import path, include
from django.conf import settings
from movie.views import home_view
from django.conf.urls.static import static

urlpatterns = [
    path('movies/', home_view, name='landing_page'),
]
