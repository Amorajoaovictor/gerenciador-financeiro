from rest_framework import serializers
from .models import User, Contribuinte




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fazer validações de campos pra api rest
        
class ContribuinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuinte
        fields = '__all__'
        # fazer validações de campos pra api rest