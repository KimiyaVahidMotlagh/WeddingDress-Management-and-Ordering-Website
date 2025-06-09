from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_measurements, name='submit_measurements'),
    path('recommendations/', views.show_recommendations, name='show_recommendations'),
]
