from django.urls import path
from . import views

app_name = 'recommendation'

urlpatterns = [
    path('', views.recommendation_view, name='recommendation'),
    path('generate/', views.generate_recommendation, name='generate'),
]
