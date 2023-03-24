from django.shortcuts import render
from .serializer import SpamSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here. 
@api_view(['POST'])
def spamEmail(request):
    serializer=SpamSerializer(data=request.data)
    serializer.is_valid()
    return Response({"emailid":serializer.emailid, "spam":True,"spamsReported":130,"confidenceScore":90})

