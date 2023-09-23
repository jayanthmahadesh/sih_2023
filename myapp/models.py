from django.db import models
from django.contrib.auth.hashers import make_password

class CustomUser(models.Model):
    unique_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    aadhar_number = models.IntegerField(unique=True)
    password = models.CharField(max_length=128)  # Store the hashed password
    gender = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        # Hash the password before saving it to the database
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name
class CaseList(models.Model):
    user_id = models.CharField(max_length=1000)
    Case_Id = models.AutoField(primary_key=True)
    Short_Case_Name = models.CharField(max_length=100)
    Case_type = models.CharField(max_length=100)
    matter = models.CharField(max_length=100)
    Petitioner = models.CharField(max_length=100)
    Respondent = models.CharField(max_length=100)
    Court_of_origin = models.CharField(max_length=100)
    Decision : models.CharField(max_length=10,default="Pending")
    Case_description = models.CharField(max_length=1000)
    critical_score = models.IntegerField()
    def __str__(self):
        return self.Short_Case_Name