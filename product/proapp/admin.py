from django.contrib import admin

from proapp.models import*
class prodb_admin(admin.ModelAdmin):
    prolist=["sl_no","proname","description","price","discount"]
admin.site.register(prodb,prodb_admin)