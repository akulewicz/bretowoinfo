from unicodedata import category
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-published_date')
    city_category = Category.objects.get(name='Z miasta')
    context = {
        'posts': posts,
        'city_category': city_category
    }

    return render(request, 'blog/posts_list.html', context )

def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all().order_by('-published_date')[:5]
    context = {
        'posts': posts,
        'post': post
    }
    return render(request, 'blog/post.html', context)