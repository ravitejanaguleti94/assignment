from django.urls import path
from . import views


urlpatterns = [
    path('doctor_home/',views.doctor_home,name='doctor-home'),
    path('doctor-details/<int:department_id>/',views.doctor_details,name='doctor-app-details'),
    path('doctor-signin/<int:doctor_id>/',views.doctor_signin,name="doctor-signin"),
    path('call-next-patient/<int:doctor_id>/',views.next,name="call-next-patient"),
    path('reset/<int:doctor_id>/',views.reset,name='reset'),

]