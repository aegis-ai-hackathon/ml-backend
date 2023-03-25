from django.contrib import admin
from .models import SpamReportModel
class SpamAdmin(admin.ModelAdmin):
    class Meta:
        model=SpamReportModel
# Register your models here.
admin.site.register(SpamReportModel,SpamAdmin)