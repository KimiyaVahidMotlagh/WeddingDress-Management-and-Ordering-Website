from django.urls import path
from .views import booking_page, create_booking, my_bookings

urlpatterns = [
    path("", booking_page, name="booking_page"),
    path("create/", create_booking, name="create_booking"),
    path("my/", my_bookings, name="my_booking"),
]
