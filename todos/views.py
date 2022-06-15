# from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView

from todos.models import TodoList

# Create your views here.


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"


class TodoDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"


class TodoCreateView(CreateView):
    model = TodoList
    template_name = "todos/create.html"
    fields = ["name"]
    success_url = "/todos/"
