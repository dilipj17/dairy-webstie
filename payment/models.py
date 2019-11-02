from django.db import models
from customer.models import Customer
from django.utils import timezone
from item_register.models import Bill
from customer.models import Customer
from django.db.models.signals import pre_delete,post_save,pre_save,pre_delete
from django.dispatch import receiver

class Transections(models.Model):
    date = models.DateField(default=timezone.now,blank=True)
    trans_id = models.CharField(max_length=10,unique=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    credit = models.BooleanField(default=False)
    amount = models.IntegerField()
    remarks = models.CharField(max_length=255,blank=True,null=True)

class Balance(models.Model):
    date = models.DateField(default=timezone.now,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    balance = models.IntegerField()

@receiver(post_save,sender=Customer)
def addCustomertobalance(sender,**kwargs):
    if kwargs['created']:
        data = kwargs['instance']
        Balance.objects.create(
            customer = data,
            balance = 0
        )
    return 0

@receiver(pre_delete,sender=Transections)
def removeBalance(sender,**kwargs):
    obj = kwargs['instance']
    balance = Balance.objects.get(customer=obj.customer)
    if obj.credit:
        balance.balance -= obj.amount
    else:
        balance.balance += obj.amount
    balance.save()


@receiver(post_save,sender=Transections)
def updateBalance(sender,**kwargs):
    if kwargs['created']:
        obj = kwargs['instance']
        balance = Balance.objects.get(customer=obj.customer)
        if obj.credit:
            balance.balance += obj.amount
        else:
            balance.balance -= obj.amount
        balance.save()        

@receiver(pre_delete,sender=Bill)
def billbalanceremove(sender,**kwargs):
    data = kwargs['instance']
    obj = Bill.objects.get(id=data.id)
    balance = Balance.objects.get(customer=obj.customer)
    if obj.is_buy:
        balance.balance -= obj.total_amount
    else:
        balance.balance += obj.total_amount
    balance.save()
