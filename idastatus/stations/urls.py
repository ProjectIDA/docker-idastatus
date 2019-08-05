from django.urls import include, path
from django.conf.urls import url
from django.views.generic import RedirectView

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stations', views.StationAPIView)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/stations', include(router.urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('stations/', views.StationListView.as_view(), name='station-list'),
    #path('station/<int:pk>', views.StationDetailView.as_view(), name='station-detail'),
]
