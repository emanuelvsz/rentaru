from rest_framework import serializers
from ..models import MovieRental

class MovieRentalSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MovieRental
        fields = '__all__'
    