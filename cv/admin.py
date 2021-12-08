from django.contrib import admin
from .models import *

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('FullName',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('ExperienceRole',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('EducationSchool',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('Skills',)

class AwardAdmin(admin.ModelAdmin):
    list_display = ('Awards',)


admin.site.register(Personal,PersonalAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Award,AwardAdmin)
