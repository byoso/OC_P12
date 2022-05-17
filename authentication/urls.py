from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # JWT Authentication:
    path(
        'obtain/',
        TokenObtainPairView.as_view(), name="token_obtain"),
    path(
        'refresh/', TokenRefreshView.as_view(),
        name="token_refresh"),
]
