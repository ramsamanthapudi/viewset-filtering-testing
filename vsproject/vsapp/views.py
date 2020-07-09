from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import viewsetserializer
from .models import Student

# Create your views here.
class viewsetclass(viewsets.ReadOnlyModelViewSet):
    serializer_class = viewsetserializer
    queryset = Student.objects.all()

#creating class which will provide all http methods and their responses
class viewsetclass( mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = viewsetserializer
    queryset = Student.objects.all()
