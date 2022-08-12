from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.bookList,name="book-list"),
    path('details/<str:pk>/', views.getBook,name="get-book"),
    path('add/', views.addBook,name="add-book"),
    path('update/<str:pk>/', views.updateBook,name="update-book"),
    path('delete/<str:pk>/', views.deleteBook,name="delete-book"),
]
