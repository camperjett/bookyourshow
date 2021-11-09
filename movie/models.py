from django.db import models

# Create your models here.
class MovieCast(models.Model):
    actor_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='cast')
    def __str__(self):
        return self.actor_name


class MovieDetail(models.Model):
    title        = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to='movie_poster')
    genre       = models.CharField(max_length=20)
    rating      = models.DecimalField(max_digits=2, decimal_places=1)
    budget       = models.DecimalField(max_digits=10, decimal_places=2)
    director     = models.CharField(max_length=20)
    producer     = models.CharField(max_length=20)
    cast = models.ManyToManyField(
        MovieCast,
        related_name='movies'
    )
    release_date = models.DateField()
    language     = models.CharField(max_length=20)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

        