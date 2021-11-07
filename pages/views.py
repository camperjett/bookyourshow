from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
