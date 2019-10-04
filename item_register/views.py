from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer

class addCustomer(LoginRequiredMixin,CreateView):
    template_name = 'add_customer.html'
    model = Customer
    fields = ['cust_id','name','father_or_husband_name','village','mobile_no']
    success_url = '/'

class CustomerListView(LoginRequiredMixin,ListView):
    model = Customer
    paginate_by = 50
    template_name = 'customer_list.html'

class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    model = Customer
    fields = ['cust_id','name','father_or_husband_name','village','mobile_no']
    success_url = 'items:view_customer'
    template_name = 'customer_update.html'

class CustomerDeleteView(LoginRequiredMixin,DeleteView):
    pass
