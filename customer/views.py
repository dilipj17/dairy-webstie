from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class addCustomer(LoginRequiredMixin,CreateView):
    template_name = 'add_customer.html'
    model = Customer
    fields = ['cust_id','name','father_or_husband_name','village','mobile_no']
    success_url = reverse_lazy('item:blank')

class CustomerListView(LoginRequiredMixin,ListView):
    model = Customer
    ordering = ['cust_id']
    paginate_by = 50
    template_name = 'customer_list.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        query = Customer.objects.all().order_by('cust_id')
        paginator = Paginator(query, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['object_list'] = file_exams
        return context

class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    model = Customer
    fields = ['cust_id','name','father_or_husband_name','village','mobile_no']
    success_url = reverse_lazy('item:blank')
    template_name = 'customer_update.html'

class CustomerDeleteView(LoginRequiredMixin,DeleteView):
    model = Customer
    success_url = reverse_lazy('cust:view')
    template_name = 'customer_delete.html'
