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

class Experience(models.Model):
    def __str__(self):
        return self.Role
    ExperienceRole = models.CharField(max_length = 200)
    ExperienceCompany = models.CharField(max_length=200)
    ExperienceTimeline = models.CharField(max_length=200)

class Education(models.Model):
    EducationSchool = models.CharField(max_length=200)
    EducationCourse = models.CharField(max_length=200)
    EducationTimeline = models.CharField(max_length=200)

class Skill(models.Model):
    Skills = models.CharField(max_length=200)
    

class Award(models.Model):
    Awards = models.CharField(max_length=200)
    

