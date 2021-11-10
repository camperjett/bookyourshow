from django.db import models

# Create your models here.
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

        