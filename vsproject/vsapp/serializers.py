from rest_framework import serializers
from .models import Student

class viewsetserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'
