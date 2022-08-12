from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.BookList.as_view(),name="book-list"),
    path('details/<str:pk>/', views.GetBook.as_view(),name="get-book"),
    path('add/', views.AddBook.as_view(),name="add-book"),
    path('update/<str:pk>/', views.UpdateBook.as_view(),name="update-book"),
    path('delete/<str:pk>/', views.DeleteBook.as_view(),name="delete-book"),
]
