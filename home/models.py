from django.db import models

class Alert(models.Model):
    Category = models.CharField(max_length=100)
    DetectionType = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Severity = models.CharField(max_length=50)
    ProcessName = models.CharField(max_length=200)
    Path = models.CharField(max_length=500)
    DetectionOrigin = models.CharField(max_length=100)
    Message = models.TextField()
    AlertTime = models.DateTimeField()
    MACAddress = models.CharField(max_length=17, blank=True, null=True)
