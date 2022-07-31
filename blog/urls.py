from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="posts_list" ),
    path('<slug:slug>', views.post_details, name="post_details" ),
    path('category/<str:category_name>/', views.categories, name="category"),
    path('posts/', views.all_posts, name="all_posts")
   
]