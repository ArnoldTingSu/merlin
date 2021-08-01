from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=225)
    series=models.CharField(max_length=225)
    isbn=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

