from django.urls import path, include
from todo import views

urlpatterns = [
    path('todo/', views.index, name="todo"),
    path('del/', views.remove, name="del"),
]