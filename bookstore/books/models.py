from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256,null=True)
    shortDescription = models.CharField(max_length=250,null=True)
    longDescription = models.TextField(null=True)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField()
    user = models.name = models.ForeignKey(User, on_delete=models.CASCAD, null=True)
    created_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

