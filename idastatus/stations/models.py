from django.db import models

# Create your models here.

class Station(models.Model):
    """Model representing a station."""
    code = models.CharField(max_length=4, help_text='Station code')
    description = models.CharField(max_length=200, help_text='Station description')
    country_code = models.CharField(max_length=2, help_text='Station\'s country code')
    
    def get_absolute_url(self):
        """Returns the url to access a particular station instance."""
        #return reverse('station-detail', args=[str(self.id)])
        return "some_url"

    def __str__(self):
        """String for representing the Model object."""
        return self.code
