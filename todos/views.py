# from django.shortcuts import render

from django.views.generic import ListView

from todos.models import TodoList

# Create your views here.


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    
