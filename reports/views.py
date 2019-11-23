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
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomerQueryForm(forms.Form):
    customer_id = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control mx-sm-3",'autocomplete':'off'}))
    From = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': "form-control mx-sm-3",'placeholder':'dd/mm/yyyy'}))
    To = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': "form-control mx-sm-3",'placeholder':'dd/mm/yyyy'}))


class LedgerQueryView(LoginRequiredMixin,FormView):
    form_class = CustomerQueryForm
    template_name = 'ledgerqueryform.html'

    def form_valid(self,form):
        formdata = form.cleaned_data
        id = formdata['customer_id']
        from_date = formdata['From']
        end_date = formdata['To']
        if from_date != None and end_date != None :
            if from_date > end_date:
                messages.error(self.request,'from date should be less than to date')
                return redirect('report:report')
        if Customer.objects.filter(cust_id = id).exists():
            customer = Customer.objects.get(cust_id = id)
            transection = Transections.objects.filter(customer=customer)
            opening_balance = 0
            if end_date != None:
                transection = transection.filter(date__lte=end_date)
            if from_date != None:
                query = transection.filter(date__lt = from_date)
                transection = transection.filter(date__gte = from_date)
                for trans in query:
                    if trans.credit:
                        opening_balance += trans.amount
                    else:
                        opening_balance -= trans.amount
            return render(self.request,'customer_ledger.html',{'transection':transection,'customer':customer,'opening_balance':opening_balance})
        messages.error(self.request,'customer id does not exists')
        return redirect('report:report')

def ledgerView(request):
    return HttpResponse('kuvxckj')
