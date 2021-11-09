from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import EditProfileForm, Dashboard

@login_required
def index(request):
	return render(request, 'user/index.html', {'form':form, 'title':'index'})


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system ####################################
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

def Logout(request):
	logout(request)
	return redirect('login')


def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exist plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})

@login_required
def edit_profile(request):
	user = request.user
	form = EditProfileForm(request.POST or None, instance=user)
	if request.method == 'POST':
		if form.is_valid():
			username = request.POST['username']
			email = request.POST['email']
			phone_no = request.POST['phone_no']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			form.save()
			return redirect('index')
	return render(request, 'user/editprofile.html', {'form':form, 'title':'Edit profile'})

class change_password(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('index')

@login_required
def dashboard(request):
	return render(request, 'user/dashboard.html', {'title': 'dashboard'})
