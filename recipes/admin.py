from django.contrib import admin
from .models import Type,Price, Recipe


# Register your models here.

admin.site.register(Type)
admin.site.register(Price)
admin.site.register(Recipe)