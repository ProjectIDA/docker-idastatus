from django.db import models

# Create your models here.

class Network(models.Model):
    """Model representing a network."""

    altcode = models.CharField(max_length=4, blank=True, null=True)
    code = models.CharField(max_length=4, blank=True,
        null=True, help_text='Network code')
    datetime = models.DateTimeField(blank=True, null=True, help_text='')
    description = models.CharField(
        max_length=100, blank=True, null=True, help_text='Network description')
    histcode = models.CharField(
        max_length=50, blank=True, null=True, help_text='')
    begt = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    endt = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')

    def __str__(self):
        """String for representing the Model object."""


class Station(models.Model):
    """Model representing a station."""
    GEODETIC_DATUM = (
        ('ONE', 'First One'),
        ('TWO', 'Second One'),
        ('THREE', 'Third One'),
    )

    addr1 = models.CharField(default=None, max_length=50, blank=True,
        null=True, help_text='Address field 1')
    addr2 = models.CharField(default=None, max_length=50, blank=True,
        null=True, help_text='Address field 2')
    altcode = models.CharField(default=None, max_length=4, blank=True, null=True)
    city = models.CharField(default=None, max_length=50, blank=True,
        null=True, help_text='City')
    code = models.CharField(max_length=6, help_text='Station code')  # datascope: sta
    country = models.CharField(default=None, 
        max_length=50, blank=True, null=True, help_text='Country')
    country_code = models.CharField(default=None, max_length=2, null=True, help_text='Station\'s country code')
    description = models.CharField(default=None, 
        max_length=100, blank=True, null=True, help_text='Station description')
    elev = models.FloatField(default=None, blank=False, null=True, help_text='Elevation')
    begt = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    endt = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    # TODO to be added at a later date
    geo_datum = models.CharField(
        choices=GEODETIC_DATUM, max_length=50, blank=True, null=True, help_text='Geodetic Positioning System')
    geology_descr = models.CharField(default=None, 
        max_length=15, blank=True, null=True, help_text='')
    histcode = models.CharField(default=None, 
        max_length=15, blank=True, null=True, help_text='')
    lat = models.FloatField(default=None, blank=False, null=True, help_text='Latitude')
    lddate = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    loc_descr = models.CharField(default=None, 
        max_length=200, blank=True, null=True, help_text='')
    lon = models.FloatField(default=None, blank=False, null=True, help_text='Longitude')
    staname = models.CharField(default=None, max_length=200, blank=True,
        null=True, help_text='')
    network_id = models.ForeignKey(Network, 
        null=True, on_delete=models.CASCADE, help_text='')
    postal_code = models.CharField(default=None, 
        max_length=15, blank=True, null=True, help_text='Postal Code')
    province = models.CharField(default=None, 
        max_length=50, blank=True, null=True, help_text='Province')
    status_code = models.CharField(default=None, 
        max_length=100, blank=True, null=True, help_text='')
    status_descr = models.CharField(default=None, 
        max_length=100, blank=True, null=True, help_text='')
    status_updated = models.CharField(default=None, 
        max_length=100, blank=True, null=True, help_text='')
    vault_descr = models.CharField(default=None, 
        max_length=200, blank=True, null=True, help_text='')

    def get_absolute_url(self):
        """Returns the url to access a particular station instance."""
        # return reverse('station-detail', args=[str(self.id)])
        return "some_url"

    def __str__(self):
        """String for representing the Model object."""
        return self.code


class ChannelEpoch(models.Model):
    """TODO: Model representing a network."""
    STORAGE = (
        ('ONE', 'First One'),
        ('TWO', 'Second One'),
        ('THREE', 'Third One'),
    )

    altcode = models.CharField(max_length=4, blank=True, null=True)
    chan = models.CharField(max_length=8, blank=True, null=True, help_text='')
    code = models.CharField(max_length=4, blank=True, null=True, help_text='ChannelEpoch code')
    edepth = models.FloatField(blank=False, null=True, help_text='')
    begt = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    endt = models.DecimalField(default=None, 
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    # flag values composed of combinations of 
    # 'C' = 'continuous' 'T' =  'triggered' 'G' =  'geophysical' 'W' =  'weather'
    flag = models.CharField(max_length=10, blank=True, null=True, help_text='')
    hang = models.DecimalField(
        max_digits=8, decimal_places=4, blank=True, null=True, help_text='')
    datetime = models.DateTimeField(blank=True, null=True, help_text='')
    description = models.CharField(
        max_length=100, blank=True, null=True, help_text='Epoch description')
    histcode = models.CharField(
        max_length=50, blank=True, null=True, help_text='')
    instype = models.CharField(
        max_length=12, blank=True, null=True, help_text='')
    station_id = models.ForeignKey(
        Station, null=True, on_delete=models.CASCADE, help_text='')
    storage_format = models.CharField(
        choices=STORAGE, max_length=50, blank=True, null=True, help_text='Storage Format')
    string = models.CharField(
        max_length=200, blank=True, null=True, help_text='')
    vang = models.DecimalField(
        max_digits=8, decimal_places=4, blank=True, null=True, help_text='')
    loc = models.CharField(
        max_length=2, blank=True, null=True, help_text='')
    nomfreq = models.FloatField(default=None, blank=False, null=True, help_text='Longitude')

    def __str__(self):
        """String for representing the Model object."""
        return self.chan

class Stage(models.Model):
    """Model representing a stage"""
    # cascade_id = models.ForeignKey() # need to find out what this key points to
    station_id = models.ForeignKey(
        Station, on_delete=models.CASCADE, help_text='')
    decifac = models.BigIntegerField()
    dfile = models.CharField(
        max_length=64, blank=True, null=True, help_text='')
    dir = models.CharField(
        max_length=128, blank=True, null=True, help_text='')
    gcalib = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    gnom = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    iunits = models.CharField(
        max_length=200, blank=True, null=True, help_text='')
    ounits = models.CharField(
        max_length=200, blank=True, null=True, help_text='')
    srate = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')

class IrisWithdraw(models.Model):
    """Model representing a IRIS withdraw"""
    chan = models.CharField(
        max_length=4, blank=True, null=True, help_text='')
    endt = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    loc = models.CharField(
        max_length=2, blank=True, null=True, help_text='')
    sta = models.CharField(
        max_length=4, blank=True, null=True, help_text='')
    begt = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    station_id = models.ForeignKey(
        Station, on_delete=models.CASCADE, help_text='')

class IrisEpoch(models.Model):
    """Model representing a IRIS epoch"""
    chan = models.CharField(
        max_length=4, blank=True, null=True, help_text='')
    decimal = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    endt = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    loc = models.CharField(
        max_length=2, blank=True, null=True, help_text='')
    sta = models.CharField(
        max_length=4, blank=True, null=True, help_text='')
    begt = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    station_id = models.ForeignKey(
        Station, on_delete=models.CASCADE, help_text='')


