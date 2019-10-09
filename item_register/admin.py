from django.contrib import admin
from .models import Item_stock,Bill,Item,temp_Item_detail,Item_detail

admin.site.register(Item_detail)
admin.site.register(Item_stock)
admin.site.register(Bill)
admin.site.register(Item)
admin.site.register(temp_Item_detail)
