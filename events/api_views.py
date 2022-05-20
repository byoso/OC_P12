from .models import (
    Client,
    Contract,
    Event,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
)


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'last_name']

    def get_queryset(self, *args, **kwargs):
        return Client.objects.all()


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'client__email', 'client__last_name',
        'amount_in_euros', 'payment_date']

    def get_queryset(self, *args, **kwargs):
        return Contract.objects.all()


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'contract__client__email', 'contract__client__last_name',
        'date'
        ]

    def get_queryset(self, *args, **kwargs):
        return Event.objects.all()
