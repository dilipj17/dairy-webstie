from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Customer

class addCustomer(CreateView):
    template_name = 'add_customer.html'
    model = Customer
    fields = ['id','name','father_or_husband_name','village','mobile_no']
    success_url = '/'

class CustomerListView(ListView):
    model = Customer
    paginate_by = 50
    template_name = 'customer_list.html'
