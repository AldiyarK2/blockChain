from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('pie/', views.piechart, name='piechart'),
    path('line/', views.linegraph, name='linegraph'),
]