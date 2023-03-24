from django.shortcuts import render
from .serializer import SpamSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ml import predict
# Create your views here. 
@api_view(['POST'])
def spamEmail(request):
    serializer=SpamSerializer(data=request.data)
    serializer.is_valid()
    pred=predict()
    return Response({"email_id":serializer.data["email_id"], "spam":bool(pred)})

