from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MovieDetail

@login_required
def home_view(request, *args, **kwargs):
    movies=MovieDetail.objects.all()
    return render(request, "movie/index.html", {'user':request.user, 'movies': movies})

@login_required
def movie_detail(request, pk):
    movie=get_object_or_404(MovieDetail, pk=pk)
    casts=movie.cast.all()
    return render(request, 'movie/movie_detail.html', {'movie': movie, 'casts': casts})

@login_required
def book_ticket(request, pk):
    movie=get_object_or_404(MovieDetail, pk=pk)
    return render(request, 'movie/book_ticket.html', {'movie': movie})

@login_required
def book_seat(request, pk, show_id):
    movie=get_object_or_404(MovieDetail, pk=pk)
    return render(request, 'movie/book_seat.html', {'movie': movie, 'show_id':show_id})

@login_required
def seat_book(request):
    print(request.data)
    return HttpResponse({})