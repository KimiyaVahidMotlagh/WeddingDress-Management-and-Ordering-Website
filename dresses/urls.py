from django.urls import path
from . import views

urlpatterns = [
    path('', views.dress_list, name='dress_list'),
    path('<int:pk>/', views.dress_detail, name='dress_detail'),
]
