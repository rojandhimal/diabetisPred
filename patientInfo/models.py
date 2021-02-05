from django.db import models

# Create your models here.

class patient(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    def _str_(self):
         return self.username
    class Meta:
        ordering = ['username']

class patientInfo(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    bp = models.IntegerField()
    ibm = models.IntegerField()
    glucose = models.IntegerField()
    sugar = models.IntegerField()
    hemoglobin = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add = True)
