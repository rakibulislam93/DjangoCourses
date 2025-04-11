from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.

class AccountUserAdmin(UserAdmin):
    list_display = ['username','id','email','user_role','is_active']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info',{'fields':('user_role',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets +(
        ('Extra Info',{'fields':('user_role',)}),
    )

admin.site.register(models.CustomUser,AccountUserAdmin)