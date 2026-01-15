from django.urls import path
from app_solar_radiate import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]