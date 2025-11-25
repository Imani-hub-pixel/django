from django.db import models

# Create your models here.
class Album(models.Model):
    title=models.CharField(max_length=200)
    artist=models.CharField(max_length=200)
    genre=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Song(models.Model):
    name=models.CharField(max_length=200)
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name