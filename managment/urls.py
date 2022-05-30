from django.urls import path, include
from rest_framework import routers
router = routers.SimpleRouter()
from .api_views import (
    EmployeeViewSet,
    AssigneEvent,
)

router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path("managment/", include(router.urls)),
    path("managment/assigne_event/<int:event_id>/to/<int:employee_id>", AssigneEvent.as_view(), name="assigne_event"),
]
