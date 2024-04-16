from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Legend(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='legend_images/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    legend = models.ForeignKey(Legend, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.legend}'

class Rating(models.Model):
    legend = models.OneToOneField(Legend, on_delete=models.CASCADE, related_name='rating')
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f'Rating for {self.legend}: {self.rating}'

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    legend = models.ForeignKey(Legend, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='legend_images/')

    def __str__(self):
        return f'Image for {self.legend}'
