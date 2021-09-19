from django.shortcuts import render, HttpResponse, redirect
from .models import *
import random
# Create your views here.


def landing(request):
    return render(request, 'snow.html')

def barracks(request):
    context = {
        "monsterSet1":random.sample(range(1,8000), 5),
        "monsterSet2":random.sample(range(1,8000), 5),
        "monsterSet3":random.sample(range(1,8000), 5),
        "monsterSet4":random.sample(range(1,8000), 5),
        "monsterSet5":random.sample(range(1,8000), 5)
    }
    return render(request, 'barracks.html', context)

def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request,'books.html', context)

def add_book(request):
    print(['title'], ['author'], ['series'], ['isbn'])
    Book.objects.create(
        title=request.POST['title'],
        author=request.POST['author'],
        series=request.POST['series'],
        isbn=request.POST['isbn']
    )
    print('book created')
    return redirect('/books')

def delete(request, id):
    selector = Book.objects.get(id=id)
    selector.delete()
    return redirect('/books')

### updating values on books ####

def update(request, id):
    selector = Book.objects.get(id=id)
    return redirect('/books')
