from django.urls import path
from .views import book_dress

urlpatterns = [
    path('dress/<int:dress_id>/book/', book_dress, name='book_dress'),
]
