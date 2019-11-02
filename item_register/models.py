from django.db import models
from django.utils import timezone
from customer.models import Customer
from django.db.models.signals import pre_delete,post_save,pre_save,pre_delete
from django.dispatch import receiver

class Item(models.Model):
    item_id = models.IntegerField(unique=True,null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(str(self.item_id) +" "+ str(self.name))

class Item_detail(models.Model):
    item = models.ForeignKey(Item,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()

class temp_Item_detail(models.Model):
    item = models.ForeignKey(Item,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()


class Bill(models.Model):
    date = models.DateField(default=timezone.now,blank = True)
    bill_no = models.CharField(unique=True,max_length=10)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    items = models.ManyToManyField(Item_detail)
    total_amount = models.IntegerField(blank=True,null=True)
    is_buy = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255,blank=True,null=True)


class Item_stock(models.Model):
    date_stock_update = models.DateField(default=timezone.now,blank=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT)
    recent_stock = models.IntegerField()
    quantity_left = models.IntegerField()

@receiver(post_save,sender=Item)
def stockItemAdd(sender,**kwargs):
    if kwargs['created']:
        data = kwargs['instance']
        Item_stock.objects.create(
            item = data,
            recent_stock = 0,
            quantity_left = 0
        )

@receiver(post_save,sender=Bill)
def stockUpdate(sender,**kwargs):
    if kwargs['created']:
        data = kwargs['instance']
        obj = Bill.objects.get(id=data.id)
        for item in temp_Item_detail.objects.all():
            stock = Item_stock.objects.get(item = item.item)
            if obj.is_buy:
                stock.recent_stock = item.quantity
                stock.quantity_left += item.quantity
            else:
                stock.quantity_left -= item.quantity
            stock.save()

@receiver(pre_delete,sender=Bill)
def updateStockOnBill(sender,**kwargs):
    obj = kwargs['instance']
    for item in obj.items.all():
        stock = Item_stock.objects.get(item = item.item)
        if obj.is_buy:
            stock.quantity_left -= item.quantity
        else:
            stock.quantity_left += item.quantity
        stock.save()

@receiver(pre_delete,sender=Bill)
def removeItemsOfBills(sender,**kwargs):
    data = kwargs['instance']
    for item in data.items.all():
        Item_detail.objects.get(id = item.pk).delete()
