from django.db import models


class Employee(models.Model):
    """
    Employee table contains the details of a employee,
    each attribute in this table represents a column in the
    database table.
    """
    emp_num = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    phone_num = models.CharField(max_length=10, blank=True)
    hire_date = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=32, blank=False)
    sex = models.CharField(max_length=16, blank=False)


class Project(models.Model):
    """

    """
    project_no = models.CharField(max_length=8, primary_key=True, blank=False)
    project_name = models.CharField(max_length=24, blank=False)
    dept_no = models.CharField(max_length=4, blank=False)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    proj_st_date = models.DateField()
    proj_en_date = models.DateField()


class Empolyee_to_project(models.Model):
    """

    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

