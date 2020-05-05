import textwrap

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.base import View
from django.views.generic import TemplateView, ListView

from rest_framework import viewsets

from .models import Station, Network
from .serializers import StationSerializer, NetworkSerializer

# Create your views here.
def index(request):
    '''View function for the home page of the site.'''

    num_networks = Network.objects.all().count()
    num_stations = Station.objects.all().count()

    context = {
        'num_networks': num_networks,
        'num_stations': num_stations,
    }

    return render(request, 'index.html', context=context)

class StationListView(generic.ListView):

    model = Station

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(StationListView, self).get_context_data(**kwargs)
        return context
    
class StationDetailView(generic.ListView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class StationAPIView(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class NetworkListView(generic.ListView):

    model = Network

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(NetworkListView, self).get_context_data(**kwargs)
        return context
    
class NetworkDetailView(generic.ListView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

class NetworkAPIView(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


