# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo")
    form = TodoForm()
    page = {
        "forms" : form, 
        "list" : item_list,
        "title" : "TODO LIST",
        }
    return render(request, "todoapp/index.html", page)

#### function to remove item ####

def remove(request, item_id): 
    item = Todo.objects.all(id= item_id) 
    item.delete() 
    messages.info(request, "item removed !!!") 
    return redirect('todo') 


