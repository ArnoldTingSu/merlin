

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('barracks', views.barracks),
    path('new_hero',views.new_hero),
    path('roll', views.roll),
    path('books', views.books),
    path('add_book', views.add_book),
    path('<id>/delete', views.delete),
    path('<id>/edit', views.update),
]
