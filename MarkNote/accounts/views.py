from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.contrib.auth import logout ,login ,authenticate

# Create your views here.

def form_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("blog:post_list")
        else:
            print("form is not valid ")
    else:
        form = RegisterForm()
    return render(request,"account/register.html",{"form":form})

def login_form(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("blog:post_list")
        else:
            error = "Email or password is incorrect."
            return render(request, 'account/login.html', {'error': error})
    return render(request,"account/login.html")

def form_logout(request):
    logout(request)
    return redirect("blog:post_list")