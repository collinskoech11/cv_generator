from django.db import models

# Create your models here.
class Personal(models.Model):
    def __str__(self):
        return self.FullName
    FullName = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    Email = models.CharField(max_length=200, null=True, blank=True)
    Socials = models.CharField(max_length=200, null=True, blank=True)
    Number = models.CharField(max_length=200, null=True, blank=True)
    Summary = models.CharField(max_length=400, null=True, blank=True)
    ExperienceRole = models.CharField(max_length = 200, null=True)
    ExperienceCompany = models.CharField(max_length=200, null=True, blank=True)
    ExperienceTimeline = models.CharField(max_length=200, null=True, blank=True)
    ExperienceDescription = models.CharField(max_length=200, null=True, blank=True)
    ExperienceRoleOne = models.CharField(max_length = 200, null=True)
    ExperienceCompanyOne = models.CharField(max_length=200, null=True, blank=True)
    ExperienceTimelineOne = models.CharField(max_length=200, null=True, blank=True)
    ExperienceDescriptionOne = models.CharField(max_length=200, null=True, blank=True)
    EducationSchool = models.CharField(max_length=200, null=True, blank=True)
    EducationCourse = models.CharField(max_length=200, null=True, blank=True)
    EducationTimeline = models.CharField(max_length=200, null=True, blank=True)
    Skills = models.CharField(max_length=200, null=True, blank=True)
    Awards = models.CharField(max_length=200, null=True, blank=True)
    

"""class Experience(models.Model):
    def __str__(self):
        return self.ExperienceRole
    ExperienceRole = models.CharField(max_length = 200)
    ExperienceCompany = models.CharField(max_length=200)
    ExperienceTimeline = models.CharField(max_length=200)
    ExperienceDescription = models.CharField(max_length=200)

class Education(models.Model):
    EducationSchool = models.CharField(max_length=200)
    EducationCourse = models.CharField(max_length=200)
    EducationTimeline = models.CharField(max_length=200)

class Skill(models.Model):
    Skills = models.CharField(max_length=200)
    

class Award(models.Model):
    Awards = models.CharField(max_length=200)
    """

