from django.db import models
from datetime import datetime, timezone

# Create your models here.

class Network(models.Model):
    code = models.CharField(max_length=4, blank=True,
        null=True, help_text='Network code')
    description = models.CharField(
        max_length=100, blank=True, null=True, help_text='Network description')
    end_date = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    start_date = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')

    def __str__(self):
        """String for representing the Network object."""
        return self.code


class Station(models.Model):
    network = models.ForeignKey(Network, null=True, on_delete=models.CASCADE, help_text='Station Network ID')
    code = models.CharField(max_length=6, help_text='Station code')  # datascope:sta
    elevation = models.FloatField(default=None, blank=True, null=True, help_text='Station Elevation') #datascope:elev
    start_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='Station Start Date') #datascope:begt
    end_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='Station End Date') #datascope:endt
    latitude = models.FloatField(default=None, blank=True, null=True, help_text='Station Latitude') #datascope:lat
    longitude = models.FloatField(default=None, blank=True, null=True, help_text='Station Longitude') #datascope:lon
    site = models.CharField(default=None, max_length=200, blank=True, null=True, help_text='Station Site Information') #datascope:staname

    def get_absolute_url(self):
        """Returns the url to access a particular station instance."""
        # return reverse('station-detail', args=[str(self.id)])
        return "some_url"

    def __str__(self):
        """String for representing the Station object."""
        return self.code

class Instype(models.Model):
    """Model representing the mapping between abbreviated 
    instrument names and a fuller name/description"""

    abbrev = models.CharField(max_length=6, blank=True, null=True, help_text='Instrument model abbreviation') #datascope:unit
    description = models.CharField(max_length=255, blank=True, null=True, help_text='Instrument full description') #datascope:desc

class ChannelEpoch(models.Model):

    instype = models.ForeignKey(Instype, null=True, on_delete=models.DO_NOTHING, help_text='Instype FK') 
    station = models.ForeignKey(Station, null=True, on_delete=models.CASCADE, help_text='Station code') #datascope:sta
    code = models.CharField(max_length=4, blank=True, null=True, help_text='Channel code') #datascope:chn
    location_code = models.CharField(max_length=2, blank=True, null=True, help_text='Location code') #datascope:loc
    start_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='Epoch Start Date')  #datascope:begt
    end_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='Epoch End Date') #datascope:endt
    depth = models.FloatField(blank=True, null=True, help_text='Instrument Overburden Depth (km)') #datascope:edepth
    azimuth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, help_text='') #datascope:hang
    dip = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, help_text='') #datascope:vang
    # types/flag values composed of combinations of 
    # 'C' = 'continuous' 'T' =  'triggered' 'G' =  'geophysical' 'W' =  'weather'
    types = models.CharField(max_length=10, blank=True, null=True, help_text='') #datascope:flag
    sensor = models.CharField(max_length=12, blank=True, null=True, help_text='') #datascope:instype
    nomfreq = models.FloatField(default=None, blank=True, null=True, help_text='Nominal frequency') #datascope:elev
    elevation = models.FloatField(default=None, blank=True, null=True, help_text='Elevation for this channel (km)') #datascope:elev
    longitude = models.FloatField(default=None, blank=True, null=True, help_text='Longitude for this channel') #datascope:lon
    latitude = models.FloatField(default=None, blank=True, null=True, help_text='Latitude for this channel') #datascope:lat
    def __str__(self):
        """String for representing the ChannelEpoch object."""
         
        # Without start/end date info, this is really a Channel identifier.
        startdt = datetime.fromtimestamp(self.start_date, tz=timezone.utc)
        enddt = datetime.fromtimestamp(self.end_date, tz=timezone.utc)
        return '.'.join([
            self.station.network.code,
            self.station.code,
            self.location_code,
            self.code,
            startdt.isoformat(),
            enddt.isoformat()
            ]).upper()

class Stage(models.Model):
    """Model representing a stage"""
    channel_epoch = models.ForeignKey(ChannelEpoch, null=True, on_delete=models.CASCADE, help_text="Channel Epoch FK") # need to find out what this key points to
    station = models.ForeignKey(Station, on_delete=models.CASCADE, help_text='Station FK')
    stage_ndx = models.IntegerField(blank=True, null=True, help_text='Stage index for parent ChannelEpoch (cascade)') #datascope:stageid
    serial_number = models.CharField(max_length=16, blank=True, null=True, help_text='Serial Number (or other identifier)') #datasceop:ssident
    decimation_factor = models.BigIntegerField() #datascope:decifac
    gnom = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='Nominal sensitivity') #datascope:gnom
    gcalib = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='Calibration sensitivity factor') #datascope:gcalib
    input_units = models.CharField(max_length=200, blank=True, null=True, help_text='') #datascope:iunits
    output_units = models.CharField(max_length=200, blank=True, null=True, help_text='') #datascope:ounits
    decimation_input_sample_rate = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:srate

    # 'sp': signal processing. Couldn't think of anything better since there are different types of files referenced here
    sp_dir = models.CharField(max_length=128, blank=True, null=True, help_text='') #datascope: dir
    sp_filename = models.CharField(max_length=64, blank=True, null=True, help_text='') #datascope: dfile

    def __str__(self):
        """String for representing the Stage object."""
        return f'{self.channel_epoch}-{self.stage_ndx}'

class IrisWithdraw(models.Model):
    """Model representing a IRIS withdraw"""
    chan = models.CharField(max_length=4, blank=True, null=True, help_text='')
    end_date = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:endt
    location_code = models.CharField(max_length=2, blank=True, null=True, help_text='')
    code = models.CharField(max_length=4, blank=True, null=True, help_text='') #datascope:sta
    start_date = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:t
    station = models.ForeignKey(Station, on_delete=models.CASCADE, help_text='')

    def __str__(self):
        """String for representing the IrisWithdraw object."""
        return self.chan

################################################################################
# IrisEpoch model
#
class IrisEpoch(models.Model):
    """Model representing a IRIS epoch"""
    chan = models.CharField(max_length=4, blank=True, null=True, help_text='')
    decimal = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    end_date = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:endt
    location_code = models.CharField(max_length=2, blank=True, null=True, help_text='')
    code = models.CharField(max_length=4, blank=True, null=True, help_text='') #datascope:sta
    start_date = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:begt
    station = models.ForeignKey(Station, on_delete=models.CASCADE, help_text='')

    def __str__(self):
        """String for representing the IrisEpoch object."""
        return self.chan
