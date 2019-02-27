from django.db import models
from django.contrib.auth.models import User


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

    def snippet(self):
        return self.body[:30] + '...'


# to add - drag and drop photo upload Javascript