from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def registration(request):
    if request.method == 'POST':
        uname=request.POST.get('fullname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password!=confirm_password:
            return HttpResponse("password and confirm password are not same")
        else:
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
            return redirect('login') 
    return render(request,'Register.html')

def index(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("username:",username,"Pass:",password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'Login.html')

def dashboard(request):
    return render(request,'Dashboard.html')  