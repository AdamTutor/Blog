from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the blog index page")

def create(request):
    return HttpResponse("This is the blog create page")

def delete(request):
    return HttpResponse("This is the blog delete page")

def edit(request):
    return HttpResponse("This is the blog edit page")
