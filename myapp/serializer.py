from rest_framework import serializers
from .models import jsondata

class backendserializer(serializers.ModelSerializer):
    class Meta:
        model = jsondata
        fields = '__all__'