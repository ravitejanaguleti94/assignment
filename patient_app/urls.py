from django.urls import path
from . import views


urlpatterns = [
    path('',views.vending_machine_home,name='home'),
    path('doctor_details/<int:department_id>/',views.doctor_details,name='doctor-details'),
    path('doctor_tokens/<int:doctor_id>/',views.doctor_tokens,name="doctor-tokens"),
    path('generate_tokens/<int:doctor_id>/',views.doctor_token_generation,name="token-generation"),

]