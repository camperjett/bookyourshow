from django.db import models
from movie.models import *

class SeatMatrix(models.Model):
    seat_row = models.SmallIntegerField()
    seat_type = models.SmallIntegerField()
    seat_no = models.CharField(max_length=5)
    seat_section = models.CharField(max_length=1)
    hall_no = models.SmallIntegerField()
    is_booked = models.BooleanField(default=False)

class ShowDetail(models.Model):
    duration = models.DurationField()
    start_time = models.DateTimeField()
    hall_no = models.ForeignKey(SeatMatrix, on_delete=models.CASCADE)
    title = models.ManyToManyField(MovieDetail, related_name='movieshows')

    def __str__(self):
        return self.title


class Theatre(models.Model):
    name = models.CharField(max_length=20)
    halls = models.ManyToManyField(ShowDetail, related_name='theatre')
    address = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    opens_at = models.TimeField(auto_now=False, auto_now_add=False)
    closes_at = models.TimeField(auto_now=False, auto_now_add=False)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
