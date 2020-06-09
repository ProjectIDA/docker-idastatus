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

class StageSerializer(serializers.ModelSerializer):
    channel_epoch_id = serializers.PrimaryKeyRelatedField(queryset=ChannelEpoch.objects.all(), source='channel_epoch.id')
    class Meta:
        model = Stage
        fields = ('id', 
                  'channel_epoch_id',
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
        
    def create(self, validated_data):
        stage = Stage.objects.create(parent=validated_data['channel_epoch']['id'], stage_name=validated_data['stage_name'])

        return stage

class ChannelEpochSerializer(serializers.ModelSerializer):
    stage_list = StageSerializer(many=True, read_only=True)
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
                  'dip',
                  'location_code',
                  'station',
                  'elevation',
                  'latitude',
                  'longitude',
                  'nomfreq',
                  'instype',
                  'stage_list',
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
