from django.shortcuts import render
from .serializer import SpamSerializer,SpamSMSSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ml import predict
# Create your views here. 
@api_view(['POST'])
def spamEmail(request):
    serializer=SpamSerializer(data=request.data)
    serializer.is_valid()
    pred=predict(serializer.data["content"])
    return Response({"email_id":serializer.data["email_id"], "spam":bool(pred)})
@api_view(['POST'])
def spamSMS(request):
    serializer=SpamSMSSerializer(data=request.data)
    serializer.is_valid()
    pred=predict(serializer.data["content"])
    return Response({"phone_no":str(serializer.data["phone_no"]), "spam":bool(pred)})
