from django.contrib import admin
from . import models
# Register your models here.

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.SpecializationModel,SpecializationAdmin)
admin.site.register(models.DesignationModel,DesignationAdmin)
admin.site.register(models.AvailableTime)
admin.site.register(models.DoctorModel)
admin.site.register(models.ReviewModel)