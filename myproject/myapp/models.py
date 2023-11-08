from django.db import models



class login(models.Model): 

    username = models.CharField(max_length=100) 

    password = models.CharField(max_length=8) 

    

# # Create your models here.

# class Employee(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     hire_date = models.DateField()
#     salary = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
    ##the __str__ method is used to display a meaningful representation of the object.

#step3
#register the model in admin panel in admin.py
#from djang.contrib import admin
#from muapp.models import Employee
#regostering models here.
#admin.site.register(Employee)

#step4
#run the development server and add employee records
#python manage.py server
#
#for admin panel create superuser.
#python manage.py createsuperuser