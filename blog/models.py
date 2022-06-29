from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(blank=False, max_length=255)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='posts/images/%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    is_fetaured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    

    def __str__(self):
        return self.title
