from django.views.generic import CreateView,ListView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item,Bill,temp_Item_detail,Item_detail
from django import forms
from customer.models import Customer
from payment.models import Balance,Transections
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib import messages

class AddItem(LoginRequiredMixin,CreateView):
    model = Item
    template_name = 'add_item.html'
    fields = ['item_id','name']
    success_url = reverse_lazy('item:blank')

class ViewItem(LoginRequiredMixin,ListView):
    model = Item
    paginate_by = 50
    template_name = 'view_item.html'

    def get_context_data(self, **kwargs):
        context = super(ViewItem, self).get_context_data(**kwargs)
        query = Item.objects.all()
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

class UpdateItem(LoginRequiredMixin,UpdateView):
    model = Item
    fields = ['item_id','name']
    template_name = 'update_item.html'
    success_url = reverse_lazy('item:blank')

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
        if not temp_Item_detail.objects.all().exists():
            messages.error(self.request,"Add Some Items")
            return redirect('item:add_bill')
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
        Transections.objects.create(
            date = bill.date,
            trans_id = 'BL'+str(bill.bill_no),
            customer = bill.customer,
            credit = bill.is_buy,
            amount = bill.total_amount,
            remarks = bill.remarks
        )
        return redirect('homepage')

    def get_context_data(self,**kwargs):
        form = super(AddBill, self).get_context_data(**kwargs)
        item = temp_Item_detail.objects.all()
        return {'items':item,'form':form}

class ViewBill(LoginRequiredMixin,ListView):
    model = Bill
    paginate_by = 70
    template_name = 'viewbill.html'

    def get_context_data(self, **kwargs):
        context = super(ViewBill, self).get_context_data(**kwargs)
        query = Bill.objects.all()
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

class DeleteBill(LoginRequiredMixin,DeleteView):
    model = Bill
    template_name = 'delete_bill.html'
    success_url = reverse_lazy('item:blank')

class TempItemCreateView(CreateView):
    template_name = 'add_temp_item.html'
    model = temp_Item_detail
    fields = ['item','quantity','price']
    success_url = reverse_lazy('item:blank')

class TempItemEditView(UpdateView):
    model = temp_Item_detail
    template_name = 'update_temp_item.html'
    fields = ['item','quantity','price']
    success_url = reverse_lazy('item:blank')

class TempItemDeleteView(DeleteView):
    model= temp_Item_detail
    template_name = 'delete_temp_item.html'
    success_message = 'item deleted'
    success_url = reverse_lazy('item:blank')

def NewBill(request):
    items = temp_Item_detail.objects.all()
    items.delete()
    return redirect('item:add_bill')

def updateList(request):
    if request.method == 'GET':
        query = temp_Item_detail.objects.all()
        data = serializers.serialize('json',query)
        return HttpResponse(data)
    return JsonResponse({'error':'some problem with server RETRY!'})

def blankPage(request):
    return render(request,'blank.html')
