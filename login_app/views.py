from django.shortcuts import render
from Dota2_trader.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from .models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse


def index(request):
    return render(request,'login_page.html')
    # return HttpResponse("hello")

def forget_password(request):
    return render(request,'forget_password/forget_password.html')

def redirect_register(request):
    return render(request,'register.html')

@csrf_exempt
def log(request):
    user_email = request.POST.get("user_email")
    user_password = request.POST.get("user_password")
    user_check = User.objects.filter(user_email=user_email)
    user_pass_check = User.objects.filter(user_password=user_password)
    if user_check and user_pass_check: #user existed
       response = render(request, 'login_success.html',)

   
    else:
        if user_check:
            return render(request, 'login_fail_wrong_passw.html')
        else:
            return render(request, 'login_fail_no_acc.html')
            
    response.set_cookie('user_password',user_password)
    response.set_cookie('user_email', user_email)
	
    return response    
@csrf_exempt
def register(request):
    user_email = request.POST.get("user_email")
    user_password = request.POST.get("user_password")
    if  User.objects.filter(user_email=user_email): 
        return render(request, 'register.html', {'user_check': True})
    else:
       
       new_user = User(user_email=user_email,user_password = user_password)
       new_user.save()
      
       response = render(request, 'login_page.html',{'user_check': False})
    response.set_cookie('user_password',user_password)
    response.set_cookie('user_email', user_email)
	
    return response

def password_reset_request(request):
    
    if request.method == 'GET':
         
        subject = 'password reset'
        message = 'localhost:8000/login/password_reset_request/'
        user_email = request.GET.get("user_email")
        if not User.objects.filter(user_email=user_email).exists():
            response = render(request, 'forget_password/failed.html', {'user_email': user_email})
        else:
            send_mail(subject,
                message, EMAIL_HOST_USER, [user_email], fail_silently=False)
            
            response = render(request, 'forget_password/reset_password.html',{'user_email': user_email})
    response.set_cookie('user_password','')
    response.set_cookie('user_email', user_email)
	
    return response

def setcookie(request):
    html = HttpResponse("<h1>Setup Django Tutorial</h1>")
    html.set_cookie('mycookie', 'Hello this is your Cookies', max_age = None)
    return html




def showcookie(request):
    show = request.COOKIES['mycookie']
    html = f"<center> New Page <br>{show}</center>"
    return HttpResponse(html)


def password_reset(request):
    if request.method == 'GET':
        current_user_email = request.COOKIES['user_email']
        current_user = User.objects.get(user_email = current_user_email)
        old_user_password = current_user.user_password
   
        new_user_password = request.GET.get("user_password")
        check_user_password = request.GET.get("user_password_confirm")
        if new_user_password != check_user_password:
            html = "please re-enter the password, not the same " 
            return HttpResponse(html)
            
        elif new_user_password == old_user_password:
            html = "please re-enter the password, same password as before " 
            return HttpResponse(html)

            
        else:
            current_user.user_password = new_user_password
            current_user.save()
        return render(request, 'forget_password/reset_successed.html')





