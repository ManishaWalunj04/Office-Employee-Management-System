from django.shortcuts import render, HttpResponse,redirect,HttpResponseRedirect
from django.contrib import messages

from .models import Employee, Role, Department
from django.db.models import Q

from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')



def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, 'all_emp.html', context)



def add_emp(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == "GET":
        return render(request, 'add_emp.html')

    else:
        return HttpResponse("Employee  Has Not Been Added")





def remove_emp(request, id=0):
    if id:
     try:
            emp_to_be_remove = Employee.objects.get(id=id)
            emp_to_be_remove.delete()
            # return HttpResponse('Employee Remove successfully')
            messages.success(request, 'Employee Remove successfully')


     except:
             messages.warning(request, 'Please Enter Valid Employee Id')
             # return HttpResponse('Please Enter Valid Employee Id')

    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }

    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__name=role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('Employee Not Found')
