
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import (
    IsAuthenticated,
    )

from .models import (
    Client,
    Contract,
    Event,
)
from .serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
)
from .permisions import (
    ClientPermission,
    ContractPermission,
    EventPermission,
)


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'last_name']

    def get_queryset(self, *args, **kwargs):
        return Client.objects.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ClientPermission]
        return [permission() for permission in permission_classes]


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'client__email', 'client__last_name',
        'amount_in_euros', 'payment_date']

    def get_queryset(self, *args, **kwargs):
        return Contract.objects.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ContractPermission]
        return [permission() for permission in permission_classes]


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'contract__client__email', 'contract__client__last_name',
        'date'
        ]

    def get_queryset(self, *args, **kwargs):
        return Event.objects.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated, EventPermission]
        return [permission() for permission in permission_classes]
