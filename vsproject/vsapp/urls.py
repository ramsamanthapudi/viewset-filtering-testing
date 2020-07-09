from django.urls import path, include
from .models import Student
from .views import viewsetclass
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # creating router object and adding our view class to it
router.register(r"student", viewsetclass)

urlpatterns = [
    #path('student/', viewsetclass.as_view({'get':'list'})),
    path('', include(router.urls))
    ]
