from django.shortcuts import render
from rest_framework import viewsets
from .serializers import viewsetserializer
from .models import Student

# Create your views here.
class viewsetclass(viewsets.ReadOnlyModelViewSet):
    serializer_class = viewsetserializer
    queryset = Student.objects.all()
