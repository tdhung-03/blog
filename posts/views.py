from django.shortcuts import render, redirect
from .models import Tag, Post
from .utils import searchPost, paginatePost


# Create your views here.
def main(request):
    posts = Post.objects.all()[:5]
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
    }
    return render(request, "main.html", context)


def posts(request):
    search_query, posts = searchPost(request)
    posts = paginatePost(request, posts, 5)
    context = {
        'search_query': search_query,
        'posts': posts
    }
    return render(request, "posts.html", context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, "post.html", context)


