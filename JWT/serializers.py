from rest_framework import serializers
from .models import StreamPlatform ,WatchList

class WatchListSerialiser(serializers.ModelSerializer):
    class Meta:
        model=WatchList
        fields="__all__"

   

class StreamPlatformSerialiser(serializers.ModelSerializer):
    watchlist=WatchListSerialiser( many=True,read_only=True)
    # watchlist=serializers.StringRelatedField(many=True) //this will give you only the title of the movies
    class Meta:
        model=StreamPlatform
        fields="__all__"  
    
    
