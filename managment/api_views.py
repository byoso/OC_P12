import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated,
    )
from .serializers import EmployeeSerializer, EmployeeReadonlySerializer
from django.contrib.auth import get_user_model

from events.models import (
    Event,
    Contract,
    Client,
    EmployeeEvent,
    EmployeeContract,
    EmployeeClient,
    )


Employee = get_user_model()


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    read_only_serializer_class = EmployeeReadonlySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'username', 'last_name']

    def get_queryset(self, *args, **kwargs):
        return Employee.objects.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self. action in ['list', 'retrieve']:
            return EmployeeReadonlySerializer
        return super().get_serializer_class()


class AssigneEvent(APIView):

    def put(self, request, event_id, employee_id):
        # print(f"=== event: {event_id} employee: {employee_id} ")  # debug
        event = get_object_or_404(Event, id=event_id)
        if EmployeeEvent.objects.filter(
                date_revoked=None).filter(event=event_id).exists():
            assignment = EmployeeEvent.objects.filter(
                    date_revoked=None).get(event=event_id)
            assignment.date_revoked = datetime.datetime.now()
            assignment.save()

        if employee_id != 0:
            employee = get_object_or_404(Employee, id=employee_id)
            assignment = EmployeeEvent.objects.create(event=event)
            assignment.employee = employee
            assignment.save()
            return Response(
                f"{employee.username}({employee.id}) assigned to "
                f"'{event.name}'({event.id})")
        else:
            return Response(
                f"Event '{event.name}'({event_id}) is not assigned anymore.")


class AssigneContract(APIView):

    def put(self, request, contract_id, employee_id):
        contract = get_object_or_404(Contract, id=contract_id)
        if EmployeeContract.objects.filter(
                date_revoked=None).filter(contract=contract_id).exists():
            assignment = EmployeeContract.objects.filter(
                    date_revoked=None).get(contract=contract_id)
            assignment.date_revoked = datetime.datetime.now()
            assignment.save()

        if employee_id != 0:
            employee = get_object_or_404(Employee, id=employee_id)
            assignment = EmployeeContract.objects.create(contract=contract)
            assignment.employee = employee
            assignment.save()
            return Response(
                f"{employee.username}({employee.id}) assigned to "
                f"contract id:{contract.id}")
        else:
            return Response(
                f"Contract '{contract}'"
                f"({contract}) is not assigned anymore.")


class AssigneClient(APIView):

    def put(self, request, client_id, employee_id):
        client = get_object_or_404(Client, id=client_id)
        if EmployeeClient.objects.filter(
                date_revoked=None).filter(client=client_id).exists():
            assignment = EmployeeClient.objects.filter(
                    date_revoked=None).get(client=client_id)
            assignment.date_revoked = datetime.datetime.now()
            assignment.save()

        if employee_id != 0:
            employee = get_object_or_404(Employee, id=employee_id)
            assignment = EmployeeClient.objects.create(client=client)
            assignment.employee = employee
            assignment.save()
            return Response(
                f"{employee.username}({employee.id}) assigned to "
                f"client '{client.last_name}'({client.id})")
        else:
            return Response(
                f"Client '{client.last_name}'({client_id}) "
                "is not assigned anymore.")
