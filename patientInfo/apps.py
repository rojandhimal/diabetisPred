# from django.apps import AppConfig


# class PatientinfoConfig(AppConfig):
#     name = 'patientInfo'


from django.contrib import admin
from .models import patient

admin.site.register(patient)