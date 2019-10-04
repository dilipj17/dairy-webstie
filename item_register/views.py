from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item

class AddItem(LoginRequiredMixin,CreateView):
    model = Item
    template_name = 'add_item.html'
    fields = ['item_id','name']
    success_url = '/'

class ViewItem(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'view_item.html'

class UpdateItem(LoginRequiredMixin,UpdateView):
    model = Item
    fields = ['item_id','name']
    template_name = 'update_item.html'
    success_url = reverse_lazy('item:view')

class DeleteItem(LoginRequiredMixin,DeleteView):
    model = Item
    success_url = reverse_lazy('item:view')
    template_name = 'delete_item.html'
