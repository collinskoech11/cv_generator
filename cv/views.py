from django.http import response
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        FullName = request.POST.get('FullName',"")
        location = request.POST.get('location',"")
        Email = request.POST.get('email',"")
        Socials = request.POST.get('social',"")
        Number = request.POST.get('Number',"")
        Summary = request.POST.get('summary',"")
        ExperienceRole = request.POST.get('experiencerole',"")
        Experiencecompany = request.POST.get('experiencecompany',"")
        ExperienceTimeline = request.POST.get('experiencetimeline',"")
        ExperienceDescription = request.POST.get('experiencedescription',"")
        EducationSchool = request.POST.get('educationschool',"")
        EducationCourse = request.POST.get('educationcourse',"")
        EducationTimeline = request.POST.get('educationtimeline',"")
        Skill = request.POST.get('skills',"")
        Award= request.POST.get('awards',"")

        describe = Personal(FullName=FullName,location=location, Email=Email, Socials=Socials, Number=Number, Summary=Summary)
        describe.save()
        exp = Experience(ExperienceRole=ExperienceRole,ExperienceCompany=Experiencecompany, ExperienceTimeline=ExperienceTimeline, ExperienceDescription=ExperienceDescription)
        exp.save()
        edu = Education(EducationSchool=EducationSchool, EducationCourse=EducationCourse, EducationTimeline=EducationTimeline)
        edu.save()
        ski = Skill(Skills=Skill)
        ski.save()
        aw = Award(Awards=Award)
        aw.save()

    return render(request, 'index.html')

def Details(request):
    return render(request, 'Details.html')