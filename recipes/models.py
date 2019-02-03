from django.db import models

# Create your models here.

class Meat(models.Model):
    pass


class Vegan(models.Model):
    pass


class Five(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Ten(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Twenty(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.title

# https://stackoverflow.com/questions/40218080/how-to-add-multiple-images-to-the-django?rq=1
# https://www.youtube.com/watch?v=jjdeOp_E7OU many photos
# many to one relationship:
#  - one category meat/vegan
#  - many recipes