from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('movies/', home_view, name='landing_page'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('movie/<int:pk>/book', book_ticket, name='book_ticket'),
    path('movie/<int:pk>/book/<int:show_id>', book_seat, name='book_seat'),
    # path('movie/seatbook/', seat_book, name="seat_book")
    path('movie/book/summary', ticket_summary, name='ticket_summary'),
    path('movie/book/summary/payment', payment, name='payment'),
    
]
