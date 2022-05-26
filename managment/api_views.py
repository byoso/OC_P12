from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import (
    IsAuthenticated,
    )

from .serializers import EmployeeSerializer
from django.contrib.auth import get_user_model


Employee = get_user_model()


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'username', 'last_name']

    def get_queryset(self, *args, **kwargs):
        return Employee.objects.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
