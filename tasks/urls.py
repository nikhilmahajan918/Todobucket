from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    # this name=update_task is the name which I wrote in list.html page
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
