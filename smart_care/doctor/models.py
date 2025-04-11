from django.db import models
from django.contrib.auth.models import User
from patient.models import PatientModel
# Create your models here.

class SpecializationModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self) -> str:
        return self.name


class DesignationModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class DoctorModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doctor/images/")
    designation = models.ManyToManyField(DesignationModel)
    specialization = models.ManyToManyField(SpecializationModel)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr.{self.user.first_name } { self.user.last_name}"


# review er jonno kora hoyeche...

STAR_CHOICES = {
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
    
    
}

class ReviewModel(models.Model):
    reviewer = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=20,choices=STAR_CHOICES)


    def __str__(self) -> str:
        return f"Patient : {self.reviewer.user.first_name} ; Doctor : {self.doctor.user.username}"


