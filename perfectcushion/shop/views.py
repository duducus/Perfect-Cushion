from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text_var = 'This is my first Django App Web Page.'
    return HttpResponse(text_var)
