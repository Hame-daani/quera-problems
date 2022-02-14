from django.db import models
from account.models import User

STATUS_CHOICES = (
    ('p', "publish"),
    ('d', "draft")
)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='d')

    def __str__(self):
        return self.title
