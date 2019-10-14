from django.db import models
from customer.models import Customer
from django.utils import timezone

class Transections(models.Model):
    date = models.DateField(default=timezone.now,blank=True)
    trans_id = models.CharField(max_length=10,unique=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    take_money = models.BooleanField(default=False)
    amount = models.IntegerField()
    remarks = models.CharField(max_length=255,blank=True,null=True)

class Balance(models.Model):
    date = models.DateField(default=timezone.now,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    balance = models.IntegerField()
