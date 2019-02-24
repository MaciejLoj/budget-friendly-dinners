from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request,'about.html')

def homepage(request):
    return render(request,'homepage.html')


