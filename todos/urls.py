from django.urls import path

from todos.views import (
    TodoDetailView,
    TodoListView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="list_todos"),
    path("<int:pk>/", TodoDetailView.as_view(), name="show_todolist"),
]
