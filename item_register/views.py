from django.views.generic import CreateView,ListView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item,Bill,temp_Item_detail,Item_detail
from django import forms
from customer.models import Customer
from bootstrap_modal_forms.generic import BSModalDeleteView,BSModalUpdateView,BSModalCreateView
from item_register.forms.temp_item_model import TempItemForm
from payment.models import Balance

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
    fields = ['date','bill_no','customer','is_buy','remarks']
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        items = temp_Item_detail.objects.all()
        bill = form.save()
        total_amount = 0
        for item in items:
            total_amount += (item.price*item.quantity)
            temp = Item_detail.objects.create(
                item = item.item,
                quantity =item.quantity,
                price = item.price,
            )
            bill.items.add(temp)
        bill.total_amount = total_amount
        bill.save()
        balance = Balance.objects.get(customer=bill.customer)
        if bill.is_buy:
            balance.balance += total_amount
        else:
            balance.balance -= total_amount
        balance.save()
        return redirect('homepage')

    def get_context_data(self,**kwargs):
        form = super(AddBill, self).get_context_data(**kwargs)
        item = temp_Item_detail.objects.all()
        return {'items':item,'form':form}

class ViewBill(LoginRequiredMixin,ListView):
    model = Bill
    template_name = 'viewbill.html'

class DeleteBill(LoginRequiredMixin,DeleteView):
    model = Bill
    template_name = 'delete_bill.html'
    success_url = reverse_lazy('item:view_bill')

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

def NewBill(request):
    items = temp_Item_detail.objects.all()
    items.delete()
    return redirect('item:add_bill')
