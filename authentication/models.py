from django.db import models
0
# Create your models here.
class students(models.Model):
    students_id = models.CharField(max_length=20)
    students_first_name = models.CharField(max_length=20)
    students_last_name = models.CharField(max_length=20)
    students_address = models.CharField(max_length=20)
    student_mobile =models.CharField(max_length=20)
    students_phy = models.CharField(max_length=20)
    students_chem = models.CharField(max_length=20)
    students_bio = models.CharField(max_length=20)
    students_maths = models.CharField(max_length=20)
    PCB_percentage = models.CharField(max_length=20)
    PCM_percentage = models.CharField(max_length=20)
    #action = models.C