from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import views
urlpatterns = [
    path('/email',csrf_exempt(views.spamEmail()))
]
