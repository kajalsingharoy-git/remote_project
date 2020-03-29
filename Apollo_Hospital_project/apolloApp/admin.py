from django.contrib import admin
from apolloApp.models import Patient
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=['pname','pno','pmarks']


admin.site.register(Patient,PatientAdmin)
