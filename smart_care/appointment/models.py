from django.db import models
from doctor.models import AvailableTime,DoctorModel
from patient.models import PatientModel
# Create your models here.

APPOINTMENT_STATUS = {
    ('Complete','Complete'),
    ('Running','Running'),
    ('Pending','Pending'),
}
APPOINTMENT_TYPES = {
    ('Online','Online'),
    ('Offline','Offline'),
}

class AppointmentModel(models.Model):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    appointment_types = models.CharField(choices=APPOINTMENT_TYPES,max_length=20)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS,max_length=20,default="Pending")
    symtom = models.TextField()
    time = models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"