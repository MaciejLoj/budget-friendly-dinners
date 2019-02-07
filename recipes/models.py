from django.db import models
from model_utils import Choices
from django.contrib.auth.models import User

# Create your models here.


class Type(models.Model):
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

class Price(models.Model):
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.price

class Recipe(models.Model):
    typ = models.ForeignKey(Type, default=None, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
# https://stackoverflow.com/questions/40218080/how-to-add-multiple-images-to-the-django?rq=1
# https://www.youtube.com/watch?v=jjdeOp_E7OU many photos

# drag and drop photo upload Javascript