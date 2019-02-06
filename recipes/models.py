from django.db import models
from model_utils import Choices
from django.contrib.auth.models import User

# Create your models here.


class Type(models.Model):
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

class Five(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    #author = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Ten(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    #author = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Twenty(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    #author = models.ForeignKey(User)

    def __str__(self):
        return self.title

#https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
# https://stackoverflow.com/questions/40218080/how-to-add-multiple-images-to-the-django?rq=1
# https://www.youtube.com/watch?v=jjdeOp_E7OU many photos
# many to one relationship:
#  - one category meat/vegan
#  - many recipes
# drag and drop photo upload Javascript