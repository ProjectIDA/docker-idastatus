from django.urls import include, path
from django.conf.urls import url
from django.views.generic import RedirectView

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stations', views.StationAPIView, 'Station')
router.register('networks', views.NetworkAPIView, 'Network')
router.register('channelepochs', views.ChannelEpochAPIView, 'ChannelEpoch')
router.register('instypes', views.InsTypeAPIView)
router.register('irisepochs', views.IrisEpochAPIView)
router.register('iriswithdraws', views.IrisWithdrawAPIView)
router.register('stages', views.StageAPIView)
router.register('units', views.UnitAPIView)

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('api/', include(router.urls)),
    path('api/stations', include(router.urls)),
    path('api/networks', include(router.urls)),
    path('api/channelepochs', include(router.urls)),
    path('api/instypes', include(router.urls)),
    path('api/irisepochs', include(router.urls)),
    path('api/iriswithdraws', include(router.urls)),
    path('api/stages', include(router.urls)),
    path('api/units', include(router.urls)),
    path('stations/', views.StationListView.as_view(), name='station-list'),
    path('networks/', views.NetworkListView.as_view(), name='network-list'),
    path('channelepochs/', views.ChannelEpochListView.as_view(), name='channelepoch-list'),
    path('instypes/', views.InsTypeListView.as_view(), name='instype-list'),
    path('irisepochs/', views.IrisEpochListView.as_view(), name='irisepoch-list'),
    path('iriswithdraws/', views.IrisWithdrawListView.as_view(), name='iriswithdraw-list'),
    path('stages/', views.StageListView.as_view(), name='stage-list'),
    path('units/', views.UnitListView.as_view(), name='unit-list'),
]
