# Generated by Django 3.2.9 on 2021-12-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_auto_20211210_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='EducationCourse',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='EducationSchool',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='EducationTimeline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='ExperienceCompany',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='ExperienceDescription',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='ExperienceTimeline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='FullName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Skills',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Socials',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Summary',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
