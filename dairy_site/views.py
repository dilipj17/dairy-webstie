from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def homePage(request):
    return HttpResponse('kuchh')

@login_required
def secondPage(request):
    return HttpResponse('kuchh bhi')
