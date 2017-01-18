from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("This is the blog index page")

def create(request):
    return HttpResponse("This is the blog create page")

def delete(request):
    return HttpResponse("This is the blog delete page")

def edit(request):
    return HttpResponse("This is the blog edit page")

def detail(request, id):
    return HttpResponse("<h2>Details for album id:" + str(id)+ "<h2>")

def test(request):
    all_posts = Post.objects.all()
    template = loader.get_template("Blog/index.html")
    context = {
    'all_posts': all_posts
    }
    return HttpResponse(template.render(context, request))
