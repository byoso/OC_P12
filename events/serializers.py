from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from .models import (
    Client,
    Contract,
    Event,
)


# helper
def assignee_helper(obj, filter_kwarg):
    """returns the obj's assignee or None"""
    employees = obj.assignment.filter(
        **filter_kwarg).filter(date_revoked=None)
    if len(employees) > 0:
        return employees[len(employees)-1].employee
    return


# Modified ModelSerializer
class InclusiveSerializer(ModelSerializer):
    assignee = SerializerMethodField()
    assignee_id = SerializerMethodField()

    def get_assignee(self, obj):
        label_id = self.label_getter()
        assignee = assignee_helper(obj, {label_id: obj.id})
        if assignee is None:
            return None
        return assignee.username

    def get_assignee_id(self, obj):
        label_id = self.label_getter()
        assignee = assignee_helper(obj, {label_id: obj.id})
        if assignee is None:
            return None
        return assignee.id


class ClientSerializer(InclusiveSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def label_getter(self):
        return 'client_id'


class ContractSerializer(InclusiveSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

    def label_getter(self):
        return 'contract_id'


class EventSerializer(InclusiveSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def label_getter(self):
        return 'event_id'
