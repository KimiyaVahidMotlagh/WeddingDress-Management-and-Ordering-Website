from django.urls import path
from .views import book_dress
from bookings.views import my_bookings

urlpatterns = [
    path('dress/<int:dress_id>/book/', book_dress, name='book_dress'),
]
