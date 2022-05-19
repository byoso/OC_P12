from django.urls import path, include
from rest_framework import routers
from .api_views import (
    ClientViewSet,
    ContractViewSet,
    EventViewSet
)

router = routers.SimpleRouter()

router.register('client', ClientViewSet, basename='client')
router.register('contract', ContractViewSet, basename='contract')
router.register('event', EventViewSet, basename='event')

urlpatterns = [
    path("events/", include(router.urls))
]
