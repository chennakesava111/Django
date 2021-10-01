from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256,null=True)
    shortDescription = models.CharField(max_length=250,null=True)
    longDescription = models.TextField(null=True)
    author = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)