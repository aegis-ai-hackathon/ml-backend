from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [
    path('email/',csrf_exempt(views.spamEmail)),
    path('sms/',csrf_exempt(views.spamSMS)),
    path('reported/',csrf_exempt(views.spamReported))
]
