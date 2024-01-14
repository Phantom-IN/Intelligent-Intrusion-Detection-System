from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('Category', 'DetectionType', 'User', 'Name', 'Severity', 'ProcessName', 'Path', 'DetectionOrigin', 'Message', 'AlertTime', 'MACAddress')
