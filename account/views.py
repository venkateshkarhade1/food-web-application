import imp
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings 
from django.core.mail import send_mail
from django.http.response import HttpResponse
import hashlib
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.contrib import messages


def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        
        else:
            messages.info(request,'failed creadential')
            return redirect('signin')
    else:
        return render(request,"signin.html")
def register(request):
    
    if request.method=='POST':
        first_name=request.POST["name"]
        username=request.POST["username"]
        email=request.POST["email"]
        passw=request.POST["password1"]
        passc=request.POST["password2"]
        
        if passw==passc:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=passw,email=email,first_name=first_name)
                user.save()
                if User.objects.filter(email=email).exists():
                    send_mail('your account has been created sucessfully','Now you can enjoy',settings.EMAIL_HOST_USER,[email],fail_silently=False,)
                    return redirect('signin')
                else:
                    return redirect('signin')
        else:
               
            messages.info(request,'password not matched')
            return redirect('signup')
    else:
        return render(request,"signup.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def forget_password_done(request):
    return render(request,"forget_password_done.html")

def forget_password(request):
    if request.method == "POST":
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            uid = User.objects.get(email=email)
            url = f'http://127.0.0.1:8000/account/change_password/{uid.profile.uuid}'
            send_mail(
            'Reset Password',
            url,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
            return redirect('forget_password_done')
        else:
            messages.error(request,'email address is not exist')
    return render(request,'forget_password.html')
###def change_password(request,uid):
    try:
        if Profile.objects.filter(uuid = uid).exists():
            if request.method == "POST":
                pass1 = 'password1'in request.POST and request.POST['password1']
                pass2 =  'password2'in request.POST and request.POST['password2']
                if pass1 == pass2:
                    p = Profile.objects.get(uuid=uid)
                    u = p.user
                    user = User.objects.get(username=u)
                    user.password = make_password(pass1)
                    user.save()
                    messages.success(request,'Password has been reset successfully')
                    return redirect('signin')
                else:
                    return HttpResponse('Two Password did not match')
                
        else:
            return HttpResponse('Wrong URL')
    except:
        return HttpResponse('Wrong URL')
    return render(request,'change_password.html')
    ###
@login_required
def delUser(request,username):
    context = {}

    try:
        user = User.object.get(username=username)
        user.is_active = False
        user.save()
        context['msg'] = 'Profile successfully disabled.'
    except User.DoesNotExist:
        redirect('signin')
    except Exception as e:
        redirect('signin')
