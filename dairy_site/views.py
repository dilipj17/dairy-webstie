from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homePage(request):
    return render(request,template_name='base_templates/dashboard.html')
