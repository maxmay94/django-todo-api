from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoItemListCreate.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', views.TodoItemRetrieveUpdateDestroy.as_view(), name='todo_retrieve_update_destroy'),
]