from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import Transections,Balance
from customer.models import Customer
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class AddTransection(LoginRequiredMixin,CreateView):
    model = Transections
    template_name = 'add_transection.html'
    success_url = '/'
    fields = ['date','customer','trans_id','credit','amount','remarks']

class ViewTransection(LoginRequiredMixin,ListView):
    model = Transections
    template_name = 'view_transections.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ViewTransection, self).get_context_data(**kwargs)
        query = Transections.objects.exclude(trans_id__icontains='BL').order_by('date')
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

class DeleteTransection(LoginRequiredMixin,DeleteView):
    model = Transections
    template_name = 'delete_transection.html'
    success_url = reverse_lazy('item:blank')

@login_required
def giveBalance(request):
    if request.method == "GET":
        id = request.GET.get('id')
        id = int(id)
        if isinstance(id,int):
            cust = Customer.objects.filter(cust_id=int(id))
            if cust.exists():
                bal = Balance.objects.get(customer=cust[0])
                data = {
                    'responce':1,
                    'amount':bal.balance,
                    'name': str(bal.customer.name)+" / "+str(bal.customer.father_or_husband_name),
                    'id':bal.customer.id,
                }
                return HttpResponse(json.dumps(data))
            else:
                return HttpResponse(json.dumps({'responce':0,'data':'customer id not exists'}))
        else:
            return HttpResponse(json.dumps({'responce':0,'data':'enter integer value'}))
