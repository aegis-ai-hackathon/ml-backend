from django.db import models

# Create your models here.
class SpamReportModel(models.Model):
    email_id=models.EmailField(null=True,default='')
    phone_no=models.IntegerField(null=True,default=0)
    spams_reported=models.IntegerField(default=0)