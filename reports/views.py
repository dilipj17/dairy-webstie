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
    customer_id = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control mx-sm-3",'autocomplete':'off'}))
    From = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': "form-control mx-sm-3",'placeholder':'dd/mm/yyyy'}))
    To = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': "form-control mx-sm-3",'placeholder':'dd/mm/yyyy'}))


class LedgerQueryView(FormView):
    form_class = CustomerQueryForm
    template_name = 'ledgerqueryform.html'

    def form_valid(self,form):
        formdata = form.cleaned_data
        print(formdata)
        id = formdata['customer_id']
        from_date = formdata['From']
        end_date = formdata['To']
        if Customer.objects.filter(cust_id = id).exists():
            customer = Customer.objects.get(cust_id = id)
            opening_balance = 0
            if(from_date == None and end_date == None):
                transection = Transections.objects.filter(customer=customer)
            else:
                query = Transections.objects.filter(customer=customer).filter(date__lt = from_date)
                for trans in query:
                    if trans.credit:
                        opening_balance += trans.amount
                    else:
                        opening_balance -= trans.amount
                transection = Transections.objects.filter(customer=customer).filter(date__range=[from_date,end_date])
            # return HttpResponse('hogya')
            return render(self.request,'customer_ledger.html',{'transection':transection,'customer':customer,'opening_balance':opening_balance})
        messages.error(self.request,'customer id does not exists')
        return redirect('report:report')

def ledgerView(request):
    return HttpResponse('kuvxckj')
