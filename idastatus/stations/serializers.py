from rest_framework import serializers
from .models import Station, Network

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id',
                  'code',
                  'description',
                  'begt',
                  'endt',
                  'lat',
                  'lon',
                  'elev',
                  'staname',
                  'lddate',
                 )


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ('id', 
                  'altcode', 
                  'code', 
                  'datetime',
                  'description',
                  'histcode',
                  'begt',
                  'endt',
                 )
