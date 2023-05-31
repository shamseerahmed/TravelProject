from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
#login page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
#register
def register(request):
    if request.method== 'POST':
        uname=request.POST ['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Pword = request.POST['password']
        C_Password = request.POST['c_password']
        if Pword==C_Password:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=Pword, first_name=first_name,
                                              last_name=last_name, email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

#logout

def logout(request):
    auth.logout(request)
    return redirect('/')