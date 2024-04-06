from django.shortcuts import render ,HttpResponse, redirect
from requests import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def HomePage(request):
    return render(request,'start.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        if password1!=password2:
            return HttpResponse('Your password is not same')
        else:                    
            my_user =User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect('login')
        
    
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Incorect usernamee or password!!')
        
    return render(request,'login.html')
def BlogPage(request):
    return render(request,'blog-single.html')
def UserGuidePage(request):
    return render(request,'user-guide.html')