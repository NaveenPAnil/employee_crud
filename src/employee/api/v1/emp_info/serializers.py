from rest_framework import serializers
from emp_info.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "auto_id",
            "employee_name",
            "email",
            "photo",
            "created_at",
            "updated_at",
            "is_deleted",
        ]
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_photo(self, value):
        max_size = 5 * 1024 * 1024  # 5 MB
        if value and value.size > max_size:
            raise serializers.ValidationError("Photo size must not exceed 5 MB.")
        return value
