from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {"all_person": all_person})

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        age = int(request.POST.get("age"))

        # บันทึกข้อมูลลงฐานข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )

        # เปลี่ยเส้นทางไปหน้าแรก
        return redirect("/")
    else:
        # แสดงฟอร์ม
        return render(request,"edit.html",{"person":person})

def delete(request, person_id):
    person = get_object_or_404(Person,pk=person_id)
    person.delete()
    return redirect("/")

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)

    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = int(request.POST.get("age"))
        person.save()
        return redirect("/")

    return render(request, 'edit.html', {"person": person})