from rest_framework import serializers
from .models import MarqueeText, About, Connections

class MarqueeTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarqueeText
        fields = ['content'] 

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['info']
        
class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connections
        fields = ['connection_url']