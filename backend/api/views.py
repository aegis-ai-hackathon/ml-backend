from django.shortcuts import render
from .serializer import SpamSerializer,SpamSMSSerializer,SpamReportEmailSerializer,SpamReportPhoneSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ml import predict,bert
from .models import SpamReportModel 
import re
# Create your views here. 
@api_view(['POST'])
def spamEmail(request):
    serializer=SpamSerializer(data=request.data)
    serializer.is_valid()
    pred,ber=predict(serializer.data["content"]),bert(serializer.data["content"])
    a=SpamReportModel.objects.all()
    val=0
    for x in a:
        if x.email_id==serializer.validated_data['email_id']:
            val=x
            break
    if not val==0:
        val=val.spams_reported
    fin_pred=((3*pred+2* round(ber)+1*val)/6)*100
    print(pred,ber,val,fin_pred)
    return Response({"phone_no":str(serializer.data["email_id"]), "spam":fin_pred>=70})
@api_view(['POST'])
def spamSMS(request):
    serializer=SpamSMSSerializer(data=request.data)
    serializer.is_valid()
    pred,ber=predict(serializer.data["content"]),bert(serializer.data["content"])
    a=SpamReportModel.objects.all()
    val=0
    for x in a:
        if x.email_id==serializer.validated_data['email_id']:
            val=x
            break
    if not val==0:
        val=val.spams_reported
    fin_pred=((3*pred+2* round(ber)+1*val)/6)*100
    return Response({"phone_no":str(serializer.data["phone_no"]), "spam":fin_pred>=70})
@api_view(['POST'])
def spamReported(request):
    #regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    a=SpamReportModel.objects.all()
    request.data['spams_reported']=1
    check=False
    val=0
    try:
        if 'email_id' in list(request.data.keys()):
            serializer=SpamReportEmailSerializer(data=request.data)
            serializer.is_valid()
            for x in a:
                if x.email_id==serializer.validated_data['email_id']:
                    check = True
                    val=x
                    break
        else:
            serializer=SpamReportPhoneSerializer(data=request.data)
            serializer.is_valid()
            for x in a:
                if x.phone_no==serializer.validated_data['phone_no']:
                    check = True
                    val=x
                    break
        if not check:
            serializer.save()
        else:
            val.spams_reported+=1
            val.save()
        return Response({"resp":"Success"})
    except Exception as e:
        return Response({"resp":"Failed", "error" : str
                         (e)})
