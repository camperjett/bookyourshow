from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MovieDetail, ShowDetail
import simplejson as json

@login_required
def home_view(request, *args, **kwargs):
    movies=MovieDetail.objects.all()
    return render(request, "movie/index.html", {'user':request.user, 'movies': movies})

@login_required
def movie_detail(request, pk):
    movie=get_object_or_404(MovieDetail, pk=pk)
    casts=movie.cast.all()
    return render(request, 'movie/movie_detail.html', {'movie': movie, 'casts': casts})
# Shows available shows
@login_required
def book_ticket(request, pk):
    movie=get_object_or_404(MovieDetail, pk=pk)
    shows=ShowDetail.objects.filter(movie=pk)
    return render(request, 'movie/book_ticket.html', {'movie': movie, 'shows': shows})
# Shows seat matrix
@login_required
def book_seat(request, pk, show_id):
    movie=get_object_or_404(MovieDetail, pk=pk)
    show = get_object_or_404(ShowDetail, pk=show_id)

    return render(request, 'movie/book_seat.html', {'movie': movie, 'show':show})

# @login_required
# def seat_book(request):
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     seats = body['array']['selected'] 
#     print(type(seats))
#     return render(request, 'movie/seat_book_summary.html', {'seats':seats})

@login_required
def ticket_summary(request):
    return render(request, 'movie/ticket_summary.html',{});

@login_required
def payment(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    return HttpResponse({})
