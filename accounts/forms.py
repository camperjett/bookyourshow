from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput, required=True)
    gender = forms.CharField(max_length=1)
    age = forms.IntegerField()
    address = forms.CharField(max_length=30)
    contact = forms.IntegerField()

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This is an invlaid username, please choose another")
        return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid user")
        return username
