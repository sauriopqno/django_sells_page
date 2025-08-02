from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=100) 
    body= models.TextField()
    slug=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)
    baner=models.ImageField(default='fall.png',blank=True)
