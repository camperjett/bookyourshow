from django.db import models
from user.models import Account

class MovieCast(models.Model):
    actor_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='cast')
    def __str__(self):
        return self.actor_name


class MovieDetail(models.Model):
    title        = models.CharField(max_length=100)
    about = models.CharField(max_length=1000, default="Super duper hit movie :)")
    photo = models.ImageField(null=True, blank=True, upload_to='movie_poster')
    cover = models.ImageField(null=True, blank=True, upload_to='movie_cover')
    genre       = models.CharField(max_length=50)
    rating      = models.DecimalField(max_digits=2, decimal_places=1)
    budget       = models.DecimalField(max_digits=15, decimal_places=2)
    director     = models.CharField(max_length=50)
    producer     = models.CharField(max_length=50)
    cast = models.ManyToManyField(
        MovieCast,
        related_name='movies'
    )
    release_date = models.DateField()
    language     = models.CharField(max_length=50)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Theatre(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    rating = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Screen(models.Model) :
    name = models.CharField(max_length=20)
    no_of_rows = models.IntegerField()
    no_of_columns = models.IntegerField()
    theatre = models.ForeignKey(Theatre,related_name="screen",on_delete=models.CASCADE)

    def __str__(self) :
        return "{x} {y} {z}".format(x=self.name,y=self.theatre.name,z=self.theatre.city)
    
class ShowDetail(models.Model):
    date = models.DateField()
    time = models.TimeField()

    price = models.IntegerField()
    screen = models.ForeignKey(Screen,related_name="show_screen", on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre,related_name="show_theatre",on_delete=models.CASCADE)

    movie = models.ForeignKey(MovieDetail,related_name="show_movie",on_delete=models.CASCADE)

    def __str__(self) :
        return "Date : {x} Time: {y} Screen: {z}".format(x=self.date,y=self.time,z=self.screen)

class Booking(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    row_num = models.PositiveSmallIntegerField(null=False, blank=False)
    col_num = models.PositiveSmallIntegerField(null=False, blank=False)
    show = models.ForeignKey(ShowDetail,related_name="booking_show",null=False,on_delete=models.CASCADE)
    user = models.ForeignKey(Account,related_name="booking_user",null=False,default=None, on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('show', 'row_num', 'col_num')
