from django.db import models

# Create your models here.

class Patient(models.Model):

    gender_choices = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    blood_group_choices = (('A positive', 'A positive'), ('B positive', 'B positive'), ('AB positive', 'AB positive'), ('O positive', 'O positive'), ('A negative', 'A negative'), ('B negative', 'B negative'), ('AB negative', 'AB negative'), ('O negative', 'O negative'))

    full_name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255, choices=gender_choices)
    age = models.IntegerField()
    blood_group = models.CharField(max_length = 255, choices=blood_group_choices)
    email = models.EmailField(unique = True)
    phoneno = models.CharField(max_length = 255)
    address = models.TextField(max_length = 500)
    password = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to="patient_profiles", default="sad.jpg")

    def __str__(self):
        return self.full_name
