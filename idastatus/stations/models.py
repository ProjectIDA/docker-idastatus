from django.db import models

# Create your models here.


class Station(models.Model):
    """Model representing a station."""
    GEODETIC_DATUM = (
        ('ONE', 'First One'),
        ('TWO', 'Second One'),
        ('THREE', 'Third One'),
    )

    addr1 = models.CharField(max_length=50, blank=True,
                             null=True, help_text='Address field 1')
    addr2 = models.CharField(max_length=50, blank=True,
                             null=True, help_text='Address field 2')
    altcode = models.CharField(max_length=4, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True,
                            null=True, help_text='City')
    code = models.CharField(max_length=4, blank=True,
                            null=True, help_text='Station code')
    country = models.CharField(
        max_length=50, blank=True, null=True, help_text='Country')
    country_code = models.CharField(
        max_length=2, blank=True, null=True, help_text='Station\'s country code')
    description = models.CharField(
        max_length=200, blank=True, null=True, help_text='Station description')
    elev = models.FloatField(blank=True, null=True, help_text='Elevation')
    end_t = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    # TODO to be added at a later date
    geo_datum = models.CharField(
        choices=GEODETIC_DATUM, max_length=50, blank=True, null=True, help_text='Geodetic Positioning System')
    geology_descr = models.CharField(
        max_length=15, blank=True, null=True, help_text='')
    histcode = models.CharField(
        max_length=15, blank=True, null=True, help_text='')
    lat = models.FloatField(blank=True, null=True, help_text='Latitude')
    loc_descr = models.CharField(
        max_length=200, blank=True, null=True, help_text='')
    lon = models.FloatField(blank=True, null=True, help_text='Longitude')
    name = models.CharField(max_length=200, blank=True,
                            null=True, help_text='')
    network_id = models.CharField(
        max_length=2, blank=True, null=True, help_text='')
    postal_code = models.CharField(
        max_length=15, blank=True, null=True, help_text='Postal Code')
    province = models.CharField(
        max_length=50, blank=True, null=True, help_text='Province')
    start_t = models.DecimalField(
        max_digits=17, decimal_places=5, blank=True, null=True, help_text='')
    status_code = models.CharField(
        max_length=100, blank=True, null=True, help_text='')
    status_descr = models.CharField(
        max_length=100, blank=True, null=True, help_text='')
    status_updated = models.CharField(
        max_length=100, blank=True, null=True, help_text='')
    vault_descr = models.CharField(
        max_length=200, blank=True, null=True, help_text='')

    def get_absolute_url(self):
        """Returns the url to access a particular station instance."""
        # return reverse('station-detail', args=[str(self.id)])
        return "some_url"

    def __str__(self):
        """String for representing the Model object."""
        return self.code


class Network(models.Model):
    """Model representing a network."""

    altcode = models.CharField(max_length=4, blank=True, null=True)
    code = models.CharField(max_length=4, blank=True,
                            null=True, help_text='Station code')
    datetime = models.DateTimeField(blank=True, null=True, help_text='')
    description = models.CharField(
        max_length=200, blank=True, null=True, help_text='Network description')
    end_date = models.DateField(
        blank=True, null=True, help_text='Last valid time for data')
    histcode = models.CharField(
        max_length=50, blank=True, null=True, help_text='')
    start_date = models.DateField(blank=True, null=True, help_text='')

    def __str__(self):
        """String for representing the Model object."""
        return self.code


class ChannelEpoch(models.Model):
    """Model representing a network."""

    altcode = models.CharField(max_length=4, blank=True, null=True)
    chn = models.CharField(max_length=4, blank=True, null=True, help_text='')
    edepth = models.FloatField(blank=True, null=True, help_text='')
    end_t = models.DateTimeField(blank=True, null=True, help_text='')
    flags = models.CharField(
        max_length=200, blank=True, null=True, help_text='')
    hang = models.DecimalField(
        max_digits=8, decimal_places=4, blank=True, null=True, help_text='')
    datetime = models.DateTimeField(blank=True, null=True, help_text='')
    description = models.CharField(
        max_length=200, blank=True, null=True, help_text='Network description')
    end_date = models.DateField(
        blank=True, null=True, help_text='Last valid time for data')
    histcode = models.CharField(
        max_length=50, blank=True, null=True, help_text='')
    start_t = models.DateTimeField(blank=True, null=True, help_text='')

    def __str__(self):
        """String for representing the Model object."""
        return self.code
