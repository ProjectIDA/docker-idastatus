from django.db import models

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
    code = models.CharField(max_length=6, help_text='Station code')  # datascope: sta
    elevation = models.FloatField(default=None, blank=False, null=True, help_text='Station Elevation') #datascope:elev
    start_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='Station Start Date') #datascope:begt
    end_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='Station End Date') #datascope:endt
    latitude = models.FloatField(default=None, blank=False, null=True, help_text='Station Latitude') #datascope:lat
    longitude = models.FloatField(default=None, blank=False, null=True, help_text='Station Longitude') #datascope:lon
    site = models.CharField(default=None, max_length=200, blank=True, null=True, help_text='Station Site Information') #datascope:staname
    network = models.ForeignKey(Network, null=True, on_delete=models.CASCADE, help_text='Station Network ID')

    def get_absolute_url(self):
        """Returns the url to access a particular station instance."""
        # return reverse('station-detail', args=[str(self.id)])
        return "some_url"

    def __str__(self):
        """String for representing the Station object."""
        return self.code


class ChannelEpoch(models.Model):
    code = models.CharField(max_length=4, blank=True, null=True, help_text='ChannelEpoch code') #datascope:chn
    depth = models.FloatField(blank=False, null=True, help_text='') #datascope:edepth
    start_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:begt
    end_date = models.DecimalField(default=None, max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:endt
    # flag values composed of combinations of 
    # 'C' = 'continuous' 'T' =  'triggered' 'G' =  'geophysical' 'W' =  'weather'
    types = models.CharField(max_length=10, blank=True, null=True, help_text='') # #datascope:flag
    azimuth = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, help_text='') #datascope:hang
    sensor = models.CharField(max_length=12, blank=True, null=True, help_text='') #datascope:instype
    station = models.ForeignKey(Station, null=True, on_delete=models.CASCADE, help_text='') #datascope:sta
    dip = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True, help_text='') #datascope:vang
    location_code = models.CharField(max_length=2, blank=True, null=True, help_text='') #datascope:loc
    elevation = models.FloatField(default=None, blank=False, null=True, help_text='Station Elevation for this channel') #datascope:elev
    latitude = models.FloatField(default=None, blank=False, null=True, help_text='Station Latitude for this channel') #datascope:lat
    longitude = models.FloatField(default=None, blank=False, null=True, help_text='Station Longitude for this channel') #datascope:lon
    def __str__(self):
        """String for representing the ChannelEpoch object."""
        return self.code

class Stage(models.Model):
    """Model representing a stage"""
    # cascade = models.ForeignKey() # need to find out what this key points to
    station = models.ForeignKey(Station, on_delete=models.CASCADE, help_text='Station ID')
    decimation_factor = models.BigIntegerField() #datascope:decifac
    data_file_name = models.CharField(max_length=64, blank=True, null=True, help_text='') #datascope: dfile
    data_dir = models.CharField(max_length=128, blank=True, null=True, help_text='') #datascope: dir
    stage_gain = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:gcalib*gnom
    input_units = models.CharField(max_length=200, blank=True, null=True, help_text='') #datascope:iunits
    output_units = models.CharField(max_length=200, blank=True, null=True, help_text='') #datascope:ounits
    decimation_input_sample_rate = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='') #datascope:srate

    def __str__(self):
        """String for representing the Stage object."""
        return self.station

class IrisWithdraw(models.Model):
    """Model representing a IRIS withdraw"""
    chan = models.CharField(max_length=4, blank=True, null=True, help_text='')
    endt = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    loc = models.CharField(max_length=2, blank=True, null=True, help_text='')
    sta = models.CharField(max_length=4, blank=True, null=True, help_text='')
    begt = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, help_text='')

    def __str__(self):
        """String for representing the IrisWithdraw object."""
        return self.chan

class IrisEpoch(models.Model):
    """Model representing a IRIS epoch"""
    chan = models.CharField(max_length=4, blank=True, null=True, help_text='')
    decimal = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    endt = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    loc = models.CharField(max_length=2, blank=True, null=True, help_text='')
    sta = models.CharField(max_length=4, blank=True, null=True, help_text='')
    begt = models.DecimalField(max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, help_text='')

    def __str__(self):
        """String for representing the IrisEpoch object."""
        return self.chan
