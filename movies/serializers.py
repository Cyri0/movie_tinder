from .models import Movie
from rest_framework.serializers import ModelSerializer

class MovieSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movie
        depth = 1
