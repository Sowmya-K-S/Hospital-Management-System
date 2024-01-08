# Generated by Django 5.0 on 2024-01-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0002_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=255)),
                ('age', models.IntegerField()),
                ('blood_group', models.CharField(choices=[('A positive', 'A positive'), ('B positive', 'B positive'), ('AB positive', 'AB positive'), ('O positive', 'O positive'), ('A negative', 'A negative'), ('B negative', 'B negative'), ('AB negative', 'AB negative'), ('O negative', 'O negative')], max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneno', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=500)),
                ('password', models.CharField(max_length=255)),
                ('profile_pic', models.FileField(default='sad.jpg', upload_to='patient_profiles')),
            ],
        ),
    ]
