from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, RegisterForm

User = get_user_model()
def register_view(request):
    form = RegisterForm(use_required_attribute=False)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first name")
        last_name = form.cleaned_data.get("last name")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        gender = form.cleaned_data.get("gender")
        age = form.cleaned_data.get("age")
        address = form.cleaned_data.get("address")
        contact = form.cleaned_data.get("contact")
        try:
            user = User.objects.create_user(username,password, gender, age, address, contact)
        except:
            user = None
            if user != None:
                login(request, user)
                return redirect("/")
            else:
                request.session['registration_error'] = 1
    return render(request, "forms.html", {"form": form})

def login_view(request):
    form = LoginForm(use_required_attribute=False)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['Invalid_user'] = 1
    return render(request, "forms.html", {"form" : form})

def logout_view(request):
    logout(request)
    return redirect("/login")