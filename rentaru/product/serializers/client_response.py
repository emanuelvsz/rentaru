from rest_framework import serializers
from ..models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class ClientForCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    cpf = serializers.CharField()
    
    