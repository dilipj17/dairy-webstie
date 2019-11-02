from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import Transections

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
