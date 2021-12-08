from django.http import response
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        FullName = request.POST.get('FullName',"")
        location = request.POST.get('location',"")
        Email = request.POST.get('Email',"")
        Socials = request.POST.get('Socials',"")
        Number = request.POST.get('Number',"")
        Summary = request.POST.get('Summary',"")
        ExperinceRole = request.POST.get('experiencerole',"")
        Experiencecompany = request.POST.get('experiencecompany',"")
        ExperienceTimeline = request.POST.get('experiencetimeline',"")
        ExperienceDescription = request.POST.get('experiencedecription',"")
        EducationSchool = request.POST.get('educationschool',"")
        EducationCourse = request.POST.get('educationcourse',"")
        educationTimeline = request.POST.get('educationtimeline',"")
        Skill = request.POST.get('skills',"")
        Award= request.POST.get('awards',"")

        describe = Personal(FullName=FullName,location=location, Eail=Email, Socials=Socials, Number=Number, Summary=Summary)
        describe.save()
        describe = Personal(FullName=FullName,location=location, Eail=Email, Socials=Socials, Number=Number)
        describe.save()

    return render(request, 'index.html')

def Details(request):
    return render(request, 'Details.html')