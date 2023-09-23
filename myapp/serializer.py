from rest_framework import serializers
from .models import *

class caseserializer(serializers.ModelSerializer):
    class Meta:
        model=CaseList
        fields ='__all__'
class userserializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields ='__all__'