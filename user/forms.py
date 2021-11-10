from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length=20, required=False)
	first_name = forms.CharField(max_length=20, required=False)
	last_name = forms.CharField(max_length=20, required=False)
	photo = forms.ImageField(required=False)
	age = forms.CharField(max_length=5, required=False)
	gender = forms.CharField(max_length=10, required=False)
	address = forms.CharField(max_length=30, required=False)
	class Meta:
		model = User
		fields = ['username', 'email','first_name', 'last_name', 'age', 'gender', 'address', 'phone_no']
	def get_object(self):
		return self.request.user
	
class Dashboard():
	pass
