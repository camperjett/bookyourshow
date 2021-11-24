from django.shortcuts import render
from user.models import Account

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name, 'user': request.user
    })
