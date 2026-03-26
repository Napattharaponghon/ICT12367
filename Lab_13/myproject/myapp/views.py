from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Person, Department
from django.db.models import Q
from django.http import JsonResponse

def index(request):
    all_person = Person.objects.all()
    query = request.GET.get('q')

    if query:
        # ตรวจสอบว่า query เป็นตัวเลขหรือไม่ เพื่อป้องกัน Error เวลาค้นหาอายุ
        if query.isdigit():
            all_person = all_person.filter(Q(name__icontains=query) | Q(age=query))
        else:
            all_person = all_person.filter(
                Q(name__icontains=query) | 
                Q(department__deptName__icontains=query) |
                Q(department__location__icontains=query)
            )
    
    return render(request, 'index.html', {"all_person": all_person})

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        dept_id = request.POST.get("department")

        # แก้ไขจุดนี้: ใช้ department_id เพื่อระบุ ID ของ ForeignKey
        person = Person.objects.create(
            name=name,
            age=int(age) if age else 0,
            department_id = dept_id if dept_id else None 
        )

        return redirect("/")
    else:
        departments = Department.objects.all()
        # เพิ่มการส่ง departments ไปที่หน้า form ด้วย เพื่อให้เลือกแผนกได้ตอนสร้างครั้งแรก
        return render(request, "form.html", {"person": None, "departments": departments})

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        dept_id = request.POST.get("department")

        person.name = name
        person.age = int(age) if age else person.age
        person.department_id = dept_id if dept_id else None
        person.save()
        
        return redirect("/")
    else:
        departments = Department.objects.all() 
        return render(request, 'edit.html', {"person": person, "departments": departments})
    
def add_department_api(request):
    if request.method == "POST":
        deptName = request.POST.get("deptName")
        location = request.POST.get("location")
        
        if deptName:
            # สร้างแผนกใหม่
            new_dept = Department.objects.create(deptName=deptName, location=location)
            return JsonResponse({
                "success": True,
                "id": new_dept.id,
                "deptName": new_dept.deptName
            })
        return JsonResponse({"success": False, "error": "กรุณากรอกชื่อแผนก"})
    return JsonResponse({"success": False, "error": "Invalid request"})