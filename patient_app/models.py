from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Departments'



    def __str__(self):
        return self.name


class Doctors(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)
    tokens = models.TextField(blank=True)
    current_token = models.CharField(max_length=10,blank=True)
    next_token = models.CharField(max_length=10,blank=True)

    class Meta:
        verbose_name_plural = "Doctors"


    def doctor_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.doctor_name()
