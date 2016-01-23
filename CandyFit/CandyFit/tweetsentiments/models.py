from django.db import models
from mongoengine import *

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')



class candidate(Document):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Job_Title = models.CharField(max_length=100)
    Cover_Title = models.CharField(max_length=1000)
    Extra_Curricular = models.CharField(max_length=100)
    Social_Profile = models.CharField(max_length=100)

class companyinfo(Document):
    Company_id = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    Job_Title = models.CharField(max_length=100)
    Company_Name = models.CharField(max_length=1000)
    Perks = models.CharField(max_length=100)
    Activities = models.CharField(max_length=1000)



