from django.db import models
from django.contrib.auth.models import User

########################

from django.db.models.signals import post_save
from django.dispatch import receiver

########################


class Director(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    poster_image = models.ImageField(upload_to='static/images/posters/', blank=True, null=True)
    average_rate = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    star_choices = [
        (1,"*"),
        (2,"**"),
        (3,"***"),
        (4,"****"),
        (5,"*****")
    ]
    
    stars = models.IntegerField(choices=star_choices)


@receiver(post_save, sender=Rating)
def updateMoveRating(sender, instance, **kwargs):
    movie = instance.movie

    sum = 0
    count = 0

    for rating in Rating.objects.all():
        sum += rating.stars
        count += 1
    
    movie.average_rate = sum / count
    movie.save()
