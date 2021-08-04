

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('books', views.books),
    path('add_book', views.add_book),
    path('<id>/delete', views.delete),
]
