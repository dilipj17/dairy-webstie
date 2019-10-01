from django.db import models
from django.utils import timezone

class Customer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=25)
    father_or_husband_name = models.CharField(max_length=25)
    village = models.CharField(max_length=25)
    mobile_no = models.IntegerField(null=True,blank=True)

class Item(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=25)

class Item_detail(models.Model):
    item = models.ForeignKey(Item,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_buy = models.BooleanField(default=False)


class Bill(models.Model):
    date = models.DateField(default=timezone.now,blank = True)
    bill_no = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    items = models.ManyToManyField(Item_detail)


class Item_stock(models.Model):
    date_stock_update = models.DateField(default=timezone.now,blank=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT)
    recent_stock = models.IntegerField()
    quantity_left = models.IntegerField()
