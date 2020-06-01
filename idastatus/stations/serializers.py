from rest_framework import serializers
from .models import Station, Network, ChannelEpoch, Instype, IrisEpoch, \
    IrisWithdraw, Stage

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

class InsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instype
        fields = ('id', 
                  'abbrev',
                  'description',
                 )

class IrisEpochSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrisEpoch
        fields = ('id', 
                  'chan',
                  'decimal',
                  'end_date',
                  'location_code',
                  'code',
                  'start_date',
                  'station',
                 )

class IrisWithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrisWithdraw
        fields = ('id', 
                  'chan',
                  'start_date',
                  'end_date',
                  'location_code',
                  'code',
                  'station',
                 )

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 
                  'channel_epoch',
                  'station',
                  'stage_ndx',
                  'serial_number',
                  'decimation_factor',
                  'gnom',
                  'gcalib',
                  'input_units',
                  'output_units',
                  'decimation_input_sample_rate',
                  'sp_dir',
                  'sp_filename',
                 )
