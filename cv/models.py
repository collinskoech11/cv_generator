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