from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemListCreate(generics.ListCreateAPIView):
    print('TodoItemListCreate called')
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    print('TodoItemRetrieveUpdateDestroy called')
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer