from django.http import response
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Details(request):
    return render(request, 'Details.html')