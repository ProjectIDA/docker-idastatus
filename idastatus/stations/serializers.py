from rest_framework import serializers
from .models import Station

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
