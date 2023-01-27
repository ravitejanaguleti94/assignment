from django.shortcuts import render,redirect
from patient_app.models import Departments,Doctors
from django.http import HttpResponse


def doctor_home(request):
        departments = Departments.objects.all()
        context = {
            "departments":departments,
        }
        return render(request,"doctor_app/1.doctor_home.htm",context)


def doctor_details(request,department_id):
    doctors = Doctors.objects.filter(department__id=department_id)
    context = {
        "doctors": doctors,
    }
    return render(request, "doctor_app/2.doctor_details.html", context)

def doctor_signin(request,doctor_id):
    doctor = Doctors.objects.get(id=doctor_id)
    context = {
        "doctor":doctor,
    }
    return render(request,"doctor_app/3.doctor_signin.html",context)

def next(request,doctor_id):
    if request.method == "POST":
        doctor = Doctors.objects.get(id=doctor_id)
        if doctor.current_token == "":
            token_list = doctor.tokens.split(",")
            doctor.current_token = token_list[0]
            doctor.next_token = token_list[1]
            doctor.save()
        else:
            token_list = doctor.tokens.split(",")
            present_token_index = token_list.index(doctor.current_token)
            doctor.current_token = token_list[present_token_index+1]
            doctor.next_token = token_list[present_token_index+2]
            doctor.save()
        context = {
            "doctor":doctor,
        }
        return render(request,"doctor_app/3.doctor_signin.html",context)
    else:
        doctor = Doctors.objects.get(id=doctor_id)
        context = {
            "doctor":doctor,
        }
        return render(request, "doctor_app/3.doctor_signin.html", context)


def reset(request,doctor_id):
    if request.method == "POST":
        doctor = Doctors.objects.get(id=doctor_id)
        doctor.tokens = ""
        doctor.current_token = ""
        doctor.next_token = ""
        doctor.save()
        context = {
            "doctor": doctor,
        }
        return render(request, "doctor_app/3.doctor_signin.html", context)
    else:
        doctor = Doctors.objects.get(id=doctor_id)
        context = {
            "doctor": doctor,
        }
        return render(request, "doctor_app/3.doctor_signin.html", context)
