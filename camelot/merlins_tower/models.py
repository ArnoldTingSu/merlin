from django.db import models
from django.db.models.fields.reverse_related import ManyToOneRel

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=225)
    series=models.CharField(max_length=225)
    isbn=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class User(models.Model):
    username=models.CharField(max_length=18)
    pin=models.IntegerField(max_length=4)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Hero(models.Model):
    name=models.CharField(max_length=12)
    health=models.IntegerField(default=100)
    attack=models.IntegerField(default=25)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Monster(models.Model):
    health=models.IntegerField(default=75)
    attack=models.IntegerField(default=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


