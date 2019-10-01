from django.contrib import admin
from .models import Customer,Item_stock,Bill,Item


admin.site.register(Customer)
admin.site.register(Item_stock)
admin.site.register(Bill)
admin.site.register(Item)
