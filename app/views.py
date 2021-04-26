from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def FirstPage(request):
    return render(request, "app/first.html")

def SecondPage(request):
    return render(request, "app/second.html")

def RegPage(request):
    return render(request, "app/reg.html")

def ShowData(request):
    data = User.objects.all()
    return render(request, "app/show.html",{'user':data})

def UpdatePage(request,pk):
    data = User.objects.get(id=pk)
    print(f"----------------DATA FOR UPDATE:{data}")
    return render(request, "app/update.html",{'data':data})

def RegUser(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pwd = request.POST['passwd']
    print(f"----------------------->FNAME---------->{fname}")
    print(f"----------------------->LNAME---------->{lname}")
    print(f"----------------------->EMAIL---------->{email}")
    print(f"----------------------->PASSWORD---------->{pwd}")
    # user = User.objects.create(modelfield = varname)
    user = User.objects.create(Fname=fname,Lname=lname,Email=email,password=pwd)
    return redirect('showdata')

def UpdateUser(request,pk):
    data = User.objects.get(id=pk)
    print(f"---------------GOT UPDATE OBJ----------->{data}")
    data.Fname = request.POST['fname'] if request.POST['fname'] else data.Fname
    data.Email = request.POST['email'] if request.POST['email'] else data.Email
    data.Lname = request.POST['lname'] if request.POST['lname'] else data.Lname
    data.password = request.POST['passwd'] if request.POST['passwd'] else data.password
    data.save()
    return redirect('showdata')

def DelUser(request,pk):
    data = User.objects.get(id=pk)
    data.delete()
    return redirect('showdata')
