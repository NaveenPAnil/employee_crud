from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from emp_info.models import Employee
from .functions import generate_auto__id
from .serializers import EmployeeSerializer


class EmployeeList(APIView):
    """
    List all employees or create a new employee.
    """
    def get(self, request, format=None):
        employees = Employee.objects.filter(is_deleted=False)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()
        # assign auto_id before save
        data["auto_id"] = generate_auto__id(Employee, "auto_id")
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    """
    Retrieve, update, or delete an employee instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk, is_deleted=False)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        # Soft delete
        employee.is_deleted = True
        employee.save()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
