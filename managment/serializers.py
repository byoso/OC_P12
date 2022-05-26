from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

Employee = get_user_model()


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(
                validated_data["password"])
        employee = super().create(validated_data)
        employee.is_active = True
        employee.save()
        return employee

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(
                validated_data["password"])
        return super().update(instance, validated_data)
