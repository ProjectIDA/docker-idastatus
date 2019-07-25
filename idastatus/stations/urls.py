from django.urls import include, path
from django.conf.urls import url
from django.views.generic import RedirectView

from stations.views import index, StationListView #, StationDetailView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('stations/', views.StationListView.as_view(), name='station-list'),
    #path('station/<int:pk>', views.StationDetailView.as_view(), name='station-detail'),
]
