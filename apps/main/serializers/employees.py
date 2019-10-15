from rest_framework import serializers
from main.models.employees import Employee
from main.serializers.file import FileSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['created_date']

    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(context=self.context)
        return super().to_representation(instance)
