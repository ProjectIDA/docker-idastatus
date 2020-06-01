import textwrap

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.base import View
from django.views.generic import TemplateView, ListView

from rest_framework import viewsets

from .models import Station, Network, ChannelEpoch, Instype, IrisEpoch, IrisWithdraw, \
    Stage
from .serializers import StationSerializer, NetworkSerializer, ChannelEpochSerializer, \
    InsTypeSerializer, IrisEpochSerializer, IrisWithdrawSerializer, StageSerializer

# Create your views here.
def index(request):
    '''View function for the home page of the site.'''

    num_networks = Network.objects.all().count()
    num_stations = Station.objects.all().count()
    num_channelepochs = ChannelEpoch.objects.all().count()

    context = {
        'num_networks': num_networks,
        'num_stations': num_stations,
        'num_channelepochs': num_channelepochs,
    }

    return render(request, 'index.html', context=context)

################################################################################
# Station classes
#
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

################################################################################
# Network classes
#
class NetworkListView(generic.ListView):

    model = Network

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(NetworkListView, self).get_context_data(**kwargs)
    
class NetworkDetailView(generic.ListView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

class NetworkAPIView(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

################################################################################
# ChannelEpoch classes
#
class ChannelEpochListView(generic.ListView):

    model = ChannelEpoch

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ChannelEpochListView, self).get_context_data(**kwargs)
        return context
    
class ChannelEpochDetailView(generic.ListView):
    queryset = ChannelEpoch.objects.all()
    serializer_class = ChannelEpochSerializer

class ChannelEpochAPIView(viewsets.ModelViewSet):
    queryset = ChannelEpoch.objects.all()
    serializer_class = ChannelEpochSerializer

################################################################################
# Instype classes
#
class InsTypeListView(generic.ListView):

    model = Instype

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(InsTypeListView, self).get_context_data(**kwargs)
        return context
    
class InsTypeDetailView(generic.ListView):
    queryset = Instype.objects.all()
    serializer_class = InsTypeSerializer

class InsTypeAPIView(viewsets.ModelViewSet):
    queryset = Instype.objects.all()
    serializer_class = InsTypeSerializer

################################################################################
# IrisEpoch classes
#
class IrisEpochListView(generic.ListView):

    model = IrisEpoch

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IrisEpochListView, self).get_context_data(**kwargs)
        return context
    
class IrisEpochDetailView(generic.ListView):
    queryset = IrisEpoch.objects.all()
    serializer_class = IrisEpochSerializer

class IrisEpochAPIView(viewsets.ModelViewSet):
    queryset = IrisEpoch.objects.all()
    serializer_class = IrisEpochSerializer

################################################################################
# IrisWithdraw classes
#
class IrisWithdrawListView(generic.ListView):

    model = IrisWithdraw

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IrisWithdrawListView, self).get_context_data(**kwargs)
        return context
    
class IrisWithdrawDetailView(generic.ListView):
    queryset = IrisWithdraw.objects.all()
    serializer_class = IrisWithdrawSerializer

class IrisWithdrawAPIView(viewsets.ModelViewSet):
    queryset = IrisWithdraw.objects.all()
    serializer_class = IrisWithdrawSerializer

################################################################################
# Stage classes
#
class StageListView(generic.ListView):

    model = Stage

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(StageListView, self).get_context_data(**kwargs)
        return context
    
class StageDetailView(generic.ListView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class StageAPIView(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

