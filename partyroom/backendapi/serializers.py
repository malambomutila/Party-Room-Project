from rest_framework import serializers
from .models import Room

# Serializer takes all the Python-related code in models.py and translates it to a JSON response

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # Define the model you want to serializer
        model = Room
        # Fields to include in the serialized output
        # Only include fields present in models.py - Room
        # Each model has a primary key represented by id
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')