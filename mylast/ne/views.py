from django.shortcuts import render
from .models import  User
# Create your views here.
def index(request):
    return render(request,"ne/index.html")
def logindata(request):
    if request.method=="POST":
        emailf=request.POST.get("emaill",False)
        passwordf=request.POST.get("passs",False)
        t=User(email=emailf,password=passwordf)
        t.save()
        return render(request,"ne/login.html")
    else:
        return render(request,"ne/login.html")