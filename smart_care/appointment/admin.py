from typing import Any
from django.contrib import admin
from .models import AppointmentModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["doctor_name","patient_name","appointment_types","appointment_status","symtom","time","cancel"]

    def doctor_name(self,obj):
        
        return obj.doctor.user.first_name
        
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appointment_status=="Running" and obj.appointment_types=="Online":
            
            subject = "Your Online Appointment is Running"
            message = render_to_string('admin_mail.html',{
                'user': obj.patient.user,
                'doctor': obj.doctor
            })
            to_mail = obj.patient.user.email

            print(to_mail)
            sent_mail = EmailMultiAlternatives(subject,to=[to_mail])
            sent_mail.attach_alternative(message,'text/html')
            sent_mail.send()


admin.site.register(AppointmentModel,AppointmentAdmin)