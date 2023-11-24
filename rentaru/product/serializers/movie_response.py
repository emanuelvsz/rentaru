from rest_framework import serializers
from ..models import Movie

class MovieSerializer(serializers.ModelSerializer):    
    cover_image = serializers.URLField(default='https://example.com/default_cover.jpg')  
    trailer_url = serializers.URLField(default='https://example.com/default_trailer.mp4')  
    class Meta:
        model = Movie
        fields = '__all__'
    