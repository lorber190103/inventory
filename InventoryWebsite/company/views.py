from django.shortcuts import render
from django.http import HttpResponse
from .models import Company

# Create your views here.

def home(request):
    message = "This is a try"
    return render(request, 'home.html', {
        "Message": message
        })

def all_companys(request):
    company_list = Company.object.all()
    return render(request, 'company/company_list.html',
        {'company_list': company_list})
