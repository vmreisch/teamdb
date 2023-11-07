from rest_framework import serializers
from .models import Athlete

class AthleteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Athlete
        fields = '__all__'