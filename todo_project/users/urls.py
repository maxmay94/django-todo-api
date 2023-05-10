from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserCreate.as_view(), name='user_create'),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user_retrieve_update_destroy'),
]