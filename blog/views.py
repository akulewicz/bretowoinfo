from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Category

# Create your views here.

def main(request):
    posts = Post.objects.all().order_by('-published_date')
    city_category = Category.objects.get(name='z miasta')
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
    category = Category.objects.get(name__iexact=category_name.replace('-', ' '))
    category_posts = category.posts.all()
    paginator = Paginator(category_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category_name': category_name.replace('-', ' '),
        'page_obj': page_obj
    }
    return render(request, 'blog/categories.html', context)


def all_posts(request):
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj
    }
    return render(request, 'blog/all_posts.html', context)