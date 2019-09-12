from main.serializers.employees import EmployeeSerializer
from main.models.employees import Employee
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class EmployeeViewSet(viewsets.ModelViewSet):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ['name', 'description']
    filter_fields = ['name', 'description']
    ordering_fields = ['id', 'created_date']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
