from django.contrib import admin
from .models import *
admin.site.register(movie_detail)
admin.site.register(theatre)
admin.site.register(show_detail)
admin.site.register(seat_matrix)
admin.site.register(ticket_offer)
admin.site.register(manager)
admin.site.register(customer)
admin.site.register(booked_seat)
admin.site.register(booking)