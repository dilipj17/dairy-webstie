from django.views.generic import CreateView,ListView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item,Bill,temp_Item_detail
from django import forms
from customer.models import Customer
from bootstrap_modal_forms.generic import BSModalDeleteView,BSModalUpdateView,BSModalCreateView
from item_register.forms.temp_item_model import TempItemForm

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

class AddBill(LoginRequiredMixin,CreateView):
    model = Bill
    template_name = 'add_bill.html'
    fields = ['date','bill_no','customer']
    success_url = reverse_lazy('homepage')

    def get_context_data(self,**kwargs):
        form = super(AddBill, self).get_context_data(**kwargs)
        item = temp_Item_detail.objects.all()
        return {'items':item,'form':form}

    def form_valid(self,form):
        form.instance.total_amount = '100'
        return super().form_valid(form)

class TempItemCreateView(BSModalCreateView):
    template_name = 'add_temp_item.html'
    form_class = TempItemForm
    success_url = reverse_lazy('item:add_bill')

class TempItemEditView(BSModalUpdateView):
    model = temp_Item_detail
    template_name = 'update_temp_item.html'
    form_class = TempItemForm
    success_url = reverse_lazy('item:add_bill')

class TempItemDeleteView(BSModalDeleteView):
    model= temp_Item_detail
    template_name = 'delete_temp_item.html'
    success_message = 'item deleted'
    success_url = reverse_lazy('item:add_bill')
