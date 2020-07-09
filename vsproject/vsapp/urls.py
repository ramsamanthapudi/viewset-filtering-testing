from django.urls import path, include
from .models import Student
from .views import viewsetclass

urlpatterns = [
    path('student/', viewsetclass.as_view({'get':'list'})),
    ]
