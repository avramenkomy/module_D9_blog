from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название поста')
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete = models.SET_NULL, related_name='posts', verbose_name='Категория')
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField(verbose_name='Содержание статьи')
    updated = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


    def __str__(self):
        return self.title
