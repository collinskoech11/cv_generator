from django.db import models

# Create your models here.
class Personal(models.Model):
    def __str__(self):
        return self.FullName
    FullName = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    social = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=200)
    PersonalSummary = models.CharField(max_length=400)

class Experiece(models.Model):
    def __str__(self):
        return self.Role
    Role = models.CharField(max_length = 200)
    CompanyName = models.CharField(max_length=200)
    Timeline = models.CharField(max_length=200)

class Education(models.Model):
    SchoolName = models.CharField(max_length=200)
    Course = models.CharField(max_length=200)
    Timeline = models.CharField(max_length=200)

class Skill(models.Model):
    Skills = models.CharField(max_length=200)
    

class Award(models.Model):
    Awards = models.CharField(max_length=200)
    

