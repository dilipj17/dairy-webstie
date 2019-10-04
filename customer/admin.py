from django.contrib import admin
from .models import Customer

class CustomerAdminView(admin.ModelAdmin):
    list_display = ('cust_id','name','father_or_husband_name','village','mobile_no')
    search_fields = ('cust_id','name')

admin.site.register(Customer,CustomerAdminView)
