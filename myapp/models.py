from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    tipo = models.IntegerField(default=2, blank=True)
    #situacao = models.TextField(default='nv',max_length=100)
    #like = models.ManyToManyField(User, default=None, blank=True, related_name='like')
    #author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='author')

