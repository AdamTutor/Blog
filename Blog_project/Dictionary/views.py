from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is the dict index url")

def choice(request):
    return HttpResponse("this is the dicitonary choice url")

def dictionary(request):
    return HttpResponse("this is the dicitonary dictionary url")

def thesaurus(request):
    return HttpResponse("this is the dicitonary thesaurus url")
