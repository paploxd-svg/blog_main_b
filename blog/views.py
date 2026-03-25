
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render 

from .models import Post, Category

#create tour nose 
def home(request):
    posts = Post.objects.filter(status=Post.ACTIVATE).order_by('-created_at')
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.ACTIVATE)

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)