from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.http import HttpResponse
from customer.models import Customer
from item_register.models import Bill
from payment.models import Transections
from django.contrib import messages
from copy import deepcopy
from django import forms

class CustomerQueryForm(forms.Form):
    customer_id = forms.IntegerField()


class LedgerQueryView(FormView):
    form_class = CustomerQueryForm
    template_name = 'ledgerqueryform.html'

    def form_valid(self,form):
        formdata = form.cleaned_data
        id = formdata['customer_id']
        if Customer.objects.filter(cust_id = id).exists():
            customer = Customer.objects.get(cust_id = id)
            transection = Transections.objects.filter(customer=customer)
            # return HttpResponse('hogya')
            return render(self.request,'customer_ledger.html',{'transection':transection,'customer':customer})
        messages.error(self.request,'customer id does not exists')
        return redirect('report:report')

def ledgerView(request):
    return HttpResponse('kuvxckj')
