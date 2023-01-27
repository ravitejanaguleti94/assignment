from django.shortcuts import render
from .models import Departments,Doctors

def vending_machine_home(request):
    departments = Departments.objects.all()
    context = {
        "departments" : departments,
    }
    return render(request,'patient_app/1.vending_machine_home.html',context)


def doctor_details(request,department_id):
    doctor_names = Doctors.objects.filter(department__id=department_id)
    context = {
        "doctors":doctor_names,
    }
    return render(request,"patient_app/2.doctor_details.html",context)

def doctor_tokens(request,doctor_id):
    doctor_tokens_all = Doctors.objects.get(id=doctor_id)
    context = {
        "doctor":doctor_tokens_all,
    }
    return render(request,"patient_app/3.doctor_tokens.html",context)

def doctor_token_generation(request,doctor_id):
    doctor = Doctors.objects.get(id=doctor_id)
    dept_code = doctor.department.name[-2:-3:-1]
    doctor_name_code = doctor.first_name[:1] + doctor.last_name[:1]
    doctor_name_code = doctor_name_code.upper()
    if doctor.tokens == "":
        token_number = 1
        generated_token = dept_code +"-"+ doctor_name_code +"-"+ str(token_number) + ","
        doctor.tokens += generated_token
        doctor.save()
        token_list = doctor.tokens.split(",")
    else:
        token_list = doctor.tokens.split(",")
        token_number = len(token_list)
        generated_token = dept_code +"-"+ doctor_name_code +"-"+ str(token_number) + ","
        doctor.tokens += generated_token
        doctor.save()
        token_list = doctor.tokens.split(",")
    context = {
        "doctor": doctor,
        "generated_token":token_list[len(token_list)-2],
    }
    return render(request,"patient_app/4.doctor_token_generation.html",context)

