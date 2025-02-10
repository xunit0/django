from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def room(request):
    return HttpResponse('ROOM')
    