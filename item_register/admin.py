from django.contrib import admin
from .models import Item_stock,Bill,Item,temp_Item_detail,Item_detail


class StockAdminView(admin.ModelAdmin):
    list_display = ('date_stock_update','item','recent_stock','quantity_left')


admin.site.register(Item_detail)
admin.site.register(Item_stock,StockAdminView)
admin.site.register(Bill)
admin.site.register(Item)
admin.site.register(temp_Item_detail)
