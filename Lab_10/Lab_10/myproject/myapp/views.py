from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(render,'index.html',{"all_person":all_person})

def about(request):
    return render(request,'about.html')

def form(request):
    return render(request, 'form.html')
