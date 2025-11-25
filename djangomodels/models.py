from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=200,null=True,blank=True)
    views=models.IntegerField(default=0)
    url=models.URLField(max_length=200)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
