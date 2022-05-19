from .models import (
    Client,
    Contract,
    Event,
)
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer,
)


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self, *args, **kwargs):
        return Client.objects.all()


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self, *args, **kwargs):
        return Contract.objects.all()


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self, *args, **kwargs):
        return Event.objects.all()
