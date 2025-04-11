from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ACCOUNT_ROLE = [
    ('admin','Admin'),
    ('editor','Editor'),
    ('customer','Customer'),
]

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_role = models.CharField(choices=ACCOUNT_ROLE,max_length=50,default='customer')
    
    def __str__(self):
        return self.username