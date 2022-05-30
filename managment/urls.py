from django.urls import path, include
from rest_framework import routers
router = routers.SimpleRouter()
from .api_views import (
    EmployeeViewSet,
    AssigneEvent,
    AssigneContract,
    AssigneClient,
)

router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path("managment/", include(router.urls)),
    path(
        "managment/assigne_event/<int:event_id>/to/<int:employee_id>",
        AssigneEvent.as_view(), name="assigne_event"),
    path(
        "managment/assigne_contract/<int:contract_id>/to/<int:employee_id>",
        AssigneContract.as_view(), name="assigne_contract"),
    path(
        "managment/assigne_client/<int:client_id>/to/<int:employee_id>",
        AssigneClient.as_view(), name="assigne_client"),
]
