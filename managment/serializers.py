from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

Employee = get_user_model()


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


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
        print("========", validated_data)
        if "password" in validated_data:
            validated_data["password"] = make_password(
                validated_data["password"])
        employee = super().update(instance, validated_data)
        return employee


class EmployeeReadonlySerializer(EmployeeSerializer):
    groups = serializers.SerializerMethodField()

    def get_groups(self, instance):
        queryset = instance.groups.all()
        serialization = GroupSerializer(queryset, many=True)
        return serialization.data
