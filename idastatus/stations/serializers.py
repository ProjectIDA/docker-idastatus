from rest_framework import serializers
from .models import Station, Network, ChannelEpoch

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id',
                  'code',
                  'elevation',
                  'start_date',
                  'end_date',
                  'latitude',
                  'longitude',
                  'site',
                  'network',
                 )

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ('id', 
                  'code', 
                  'description',
                  'start_date',
                  'end_date',
                 )

class ChannelEpochSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelEpoch
        fields = ('id', 
                  'code', 
                  'depth', 
                  'start_date',
                  'end_date',
                  'types',
                  'azimuth',
                  'sensor',
                  'station',
                  'dip',
                  'location_code',
                 )
