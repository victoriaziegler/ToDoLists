# from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])


class TodoUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/edit.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])


class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = "todos/delete.html"
    success_url = "/todos/"
