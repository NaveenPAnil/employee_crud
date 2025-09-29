from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    deleted_at = models.DateTimeField(db_index=True, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Employee(BaseModel):
    employee_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='employee/profile_pictures', blank=True, null=True)

    def __str__(self):
        return self.employee_name

    class Meta:
        db_table = 'emp_info_employee_detail'
        verbose_name = _('employee_detail')
        verbose_name_plural = _('employee_details')
        ordering = ('-employee_name',)
