from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=100);
    time= models.DateTimeField();
    banner=models.ImageField(default='fall.png',blank=True)



