from django.db import models
from django.utils import timezone

class Customer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    cust_id = models.IntegerField(unique=True,null=True)
    name = models.CharField(max_length=25)
    father_or_husband_name = models.CharField(max_length=25)
    village = models.CharField(max_length=25)
    mobile_no = models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ['cust_id']

    def __str__(self):
        return str(str(self.cust_id)+" "+str(self.name))
