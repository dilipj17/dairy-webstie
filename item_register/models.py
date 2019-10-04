from django.db import models
from django.utils import timezone
from customer.models import Customer

class Item(models.Model):
    item_id = models.IntegerField(unique=True,null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)

class Item_detail(models.Model):
    item = models.ForeignKey(Item,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_buy = models.BooleanField(default=False)


class Bill(models.Model):
    date = models.DateField(default=timezone.now,blank = True)
    bill_no = models.CharField(unique=True,max_length=10)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    items = models.ManyToManyField(Item_detail)
    total_amount = models.IntegerField()


class Item_stock(models.Model):
    date_stock_update = models.DateField(default=timezone.now,blank=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT)
    recent_stock = models.IntegerField()
    quantity_left = models.IntegerField()
