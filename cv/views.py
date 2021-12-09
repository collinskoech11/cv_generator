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
        Skillset = request.POST.get('skills',"")
        Awarding= request.POST.get('awards',"")

        describe = Personal(
            FullName=FullName,
            location=location, 
            Email=Email, 
            Socials=Socials, 
            Number=Number, 
            Summary=Summary,
            ExperienceRole=ExperienceRole,
            ExperienceCompany=Experiencecompany, 
            ExperienceTimeline=ExperienceTimeline, 
            ExperienceDescription=ExperienceDescription,
            EducationSchool=EducationSchool, 
            EducationCourse=EducationCourse, 
            EducationTimeline=EducationTimeline,
            Skills=Skillset,
            Awards=Awarding
            )
        describe.save()
        """ exp = Experience(ExperienceRole=ExperienceRole,ExperienceCompany=Experiencecompany, ExperienceTimeline=ExperienceTimeline, ExperienceDescription=ExperienceDescription)
        exp.save()
        edu = Education(EducationSchool=EducationSchool, EducationCourse=EducationCourse, EducationTimeline=EducationTimeline)
        edu.save()
        ski = Skill(Skills=Skillset)
        ski.save()
        aw = Award(Awards=Awarding)
        aw.save()"""

    return render(request, 'index.html')

def Details(request):
    description_objects = Personal.objects.all()
    #experience_objects = Experience.objects.all()
    #education_objects = Education.objects.all()
    #skill_objects = Skill.objects.all()
    #award_objects = Award.objects.all()
    return render(request, 'Details.html',
        {'description_objects':description_objects},
        #{'experience_objects':experience_objects},
        #{'education_objects':education_objects},
        #{'skill_objects':skill_objects}
        #{'award_objects':award_objects}
    )