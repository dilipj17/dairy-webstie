from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item_register.models import Item_stock

@login_required
def homePage(request):
    object_list = Item_stock.objects.all()
    return render(request,'base_templates/dashboard.html',{'object_list':object_list})
