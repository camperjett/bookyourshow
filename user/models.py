from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to='images')
    phone_no = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=5, null=True)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email