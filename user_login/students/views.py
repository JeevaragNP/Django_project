from django.shortcuts import render
from django.http import HttpResponse
from .models import Students


def index(request):
    students = Students.objects.all()
    return HttpResponse('hello world')


def new(request):
    return HttpResponse('New page')



