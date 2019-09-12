from rest_framework import serializers
from main.models.employees import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['created_date']