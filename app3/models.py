from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    deptno = models.IntegerField(primary_key=True, unique=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EmployeTable(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees'
    )
    empno = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    sal = models.DecimalField(max_digits=10, decimal_places=2)
    comm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hiredate = models.DateField()
    mgr = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    deptno = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees_by_deptno'
    )

    def __str__(self):
        return self.emp_name

