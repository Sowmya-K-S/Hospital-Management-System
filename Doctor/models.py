from django.db import models

class DepartmentTable(models.Model):
    dept_name = models.CharField(max_length=100)
  
    def __str__(self):
        return self.dept_name 

class DoctorTable(models.Model):
    d_name = models.CharField(max_length=100)
    special = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    y_of_exp = models.IntegerField()
    dept_id = models.ForeignKey(DepartmentTable, on_delete = models.CASCADE)

    def __str__(self):
        return self.d_name
