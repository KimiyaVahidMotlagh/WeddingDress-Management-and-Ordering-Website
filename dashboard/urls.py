from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_dashboard, name='company_dashboard'),
]
