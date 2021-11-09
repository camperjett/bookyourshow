from django.db import models
from show.models import *
from django.contrib.auth.models import User

class BookedSeat(models.Model):
    booking_time = models.DateTimeField()
    currency = models.CharField(max_length=5)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    seat_type = models.SmallIntegerField()
    rate = models.SmallIntegerField()
    title = models.OneToOneField(ShowDetail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)