from django.contrib import admin

# Register your models here.

from stations.models import Station

# admin.site.register(Station)

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass
