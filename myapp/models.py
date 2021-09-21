from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    #situacao = models.TextField(default='nv',max_length=100)
    #like = models.ManyToManyField(User, default=None, blank=True, related_name='like')
    #author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='author')
    '''
    @property
    def num_likes(self):
        return self.like.all().count()

LIKE_CHOICE = {
    ('Like','Like'),
    ('Unlike', 'Unlike')
}

class Liked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ForeignKey(Image, on_delete=models.CASCADE)
    #value = models.CharField(choices=LIKE_CHOICE, default="Like", max_length=10)
    def __str__(self):
        return str(self.imagem)'''