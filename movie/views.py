from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MovieDetail

@login_required
def home_view(request, *args, **kwargs):
    movies=MovieDetail.objects.all()
    return render(request, "movie/index.html", {'user':request.user, 'movies': movies})
