from django.urls import path, include
from rest_framework import routers
router = routers.SimpleRouter()
from .api_views import EmployeeViewSet

router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path("managment/", include(router.urls))
]
