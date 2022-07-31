from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def main(request):
    posts = Post.objects.all().order_by('-published_date')
    city_category = Category.objects.get(name='Z miasta')
    context = {
        'posts': posts,
        'city_category': city_category
    }
    return render(request, 'blog/main.html', context)


def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all().order_by('-published_date')[:5]
    context = {
        'posts': posts,
        'post': post
    }
    return render(request, 'blog/post.html', context)


def categories(request, category_name):
    category = Category.objects.get(name__iexact=category_name)
    category_posts = category.posts.all()
    context = {
        'category_name': category_name,
        'category_posts': category_posts
    }
    return render(request, 'blog/categories.html', context)

def all_posts(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/all_posts.html', {'posts': posts})