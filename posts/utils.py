from .models import Tag, Post
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchPost(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    posts = Post.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(tags__in=tags)
    )
    return search_query, posts


def paginatePost(request, posts, result):
    page = request.GET.get('page')
    paginator = Paginator(posts, result)
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
    posts = paginator.get_page(page)
    return posts
