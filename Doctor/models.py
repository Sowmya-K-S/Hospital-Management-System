from django.db import models

# Create your models here.

class DepartmentTable(models.Model):
    dept_name = models.CharField(max_length=255)
    dept_pic = models.FileField(default="g1.jpg", upload_to="dept_pics", null=True, blank=True)
    def __str__(self):
        return self.dept_name
    

class Doctor_table(models.Model):
    special_choices = (('Cardiology', 'Cardiology'), ('Skin Care', 'Skin Care'), ('Pediatrics', 'Pediatrics'))
    full_name = models.CharField(max_length = 255)
    special = models.CharField(max_length = 255, choices=special_choices)
    email = models.EmailField(unique = True)
    phoneno = models.CharField(max_length = 255)
    degree = models.CharField(max_length = 255)
    y_of_exp = models.IntegerField()
    address = models.TextField(max_length = 500)
    password = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to="patient_profiles", default="sad.jpg")
    dept = models.ForeignKey(DepartmentTable, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name