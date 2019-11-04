from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import Transections,Balance
from customer.models import Customer
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json

class AddTransection(CreateView):
    model = Transections
    template_name = 'add_transection.html'
    success_url = '/'
    fields = ['date','customer','trans_id','credit','amount','remarks']

class ViewTransection(ListView):
    model = Transections
    template_name = 'view_transections.html'

class DeleteTransection(DeleteView):
    model = Transections
    template_name = 'delete_transection.html'
    success_url = reverse_lazy('payment:view')

def giveBalance(request):
    if request.method == "GET":
        id = request.GET.get('id')
        id = int(id)
        if isinstance(id,int):
            cust = Customer.objects.filter(cust_id=int(id))
            if cust.exists():
                bal = Balance.objects.get(customer=cust[0])
                data = {
                    'responce':1,
                    'amount':bal.balance,
                    'name': str(bal.customer.name)+" / "+str(bal.customer.father_or_husband_name)
                }
                return HttpResponse(json.dumps(data))
            else:
                return HttpResponse(json.dumps({'responce':0,'data':'customer id not exists'}))
        else:
            return HttpResponse(json.dumps({'responce':0,'data':'enter integer value'}))
