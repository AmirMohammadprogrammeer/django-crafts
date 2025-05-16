from django.shortcuts import render,get_object_or_404,redirect
from .forms import FormRegisterPackage
from django.contrib import messages
from .models import Package
import jdatetime as jtime
from datetime import timedelta
# Create your views here.

def home_page(request):
    return render(request,"index.html")

def create_package(request):
    if request.method == "POST":
        form = FormRegisterPackage(request.POST)
        if form.is_valid():
            form.save()
            redirect("show")
        else:
            messages.error(request,"error")
    else:
        form = FormRegisterPackage()
    
    return render(request,"create.html",{'form':form})

def show_package(request):
    package = Package.objects.all()
    return render(request,"show_package.html",{'package':package})

def detail_package(request,id):
    package = get_object_or_404(Package,id=id)
    new_date = package.date + timedelta(days=package.duration)
    if package.date == new_date:
        package.delete()
    return render(request,"package_detail.html",{'detail':package ,"time":new_date})

def delete_package(request,id):
    package = get_object_or_404(Package,id=id)
    package.delete()
    return redirect("show")