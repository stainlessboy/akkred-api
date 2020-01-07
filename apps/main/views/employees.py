from main.serializers.employees import EmployeeSerializer
from main.models.employees import Employee
from rest_framework import viewsets, permissions


class EmployeeViewSet(viewsets.ModelViewSet):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    ordering_fields = ['-order', 'modified_date']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super(EmployeeViewSet, self).get_permissions()
