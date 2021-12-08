from django.contrib import admin
from .models import *

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('FullName',)

class ExperienceAdmin(admin.Model):
    list_display = ('Role,')

class EducationAdmin(admin.Model):
    list_display = ('SchoolName',)

class SkillAdmin(admin.Model):
    list_display = ('Skills',)

class AwardAdmin(admin.Model):
    list_display = ('Awards')


admin.site.register(Personal,PersonalAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Award,AwardAdmin)
