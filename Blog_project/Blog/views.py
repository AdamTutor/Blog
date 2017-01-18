from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post


# Create your views here.

def index(request):
    return HttpResponse("This is the blog index page")

def create(request):
    return HttpResponse("This is the blog create page")

def delete(request):
    return HttpResponse("This is the blog delete page")

def edit(request):
    return HttpResponse("This is the blog edit page")


def test(request):
    all_posts = Post.objects.all()
    return render(request, 'Blog/index.html', {'all_posts': all_posts})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'Blog/detail.html', {'post': post})
