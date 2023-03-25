from rest_framework import serializers
from .models import SpamReportModel
class SpamSerializer(serializers.Serializer):
    email_id=serializers.EmailField()
    content=serializers.CharField(max_length=10000)
class SpamSMSSerializer(serializers.Serializer):
    phone_no=serializers.IntegerField()
    content=serializers.CharField(max_length=10000)  
class SpamReportEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=SpamReportModel
        exclude=['phone_no']
class SpamReportPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=SpamReportModel
        exclude=['email_id']

#emailid
#number of spams