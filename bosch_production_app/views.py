from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from . import models

# Create your views here.
def render_signin(request):
    return render(request,'auth_templates/signin.html')

def perform_signin(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        print("Sign IN Initiated")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("admin_dashboard")
            if user.user_type == "2":
                return HttpResponse("Super Login")
            if user.user_type == "3":
                return HttpResponseRedirect("expert_dashboard")
            if user.user_type == "4":
                return HttpResponseRedirect("user_dashboard")
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")

def perform_signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def render_signup(request):
    department_objs = models.Department.objects.all()
    context = {
        'departments':department_objs
    }
    return render(request, "auth_templates/signup.html",context)

def perform_signup(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        print("Sign UP Initiated")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        employeenumber = request.POST.get("employeenumber")
        department_id = request.POST.get("department_id")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        if confirm != password:
            messages.error(request,'Invalid password confirmation')
            return HttpResponseRedirect(reverse('signup'))
        else:
            try:
                user_obj = models.CustomUser.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email,employee_number=employeenumber,password=password, user_type=4)
                user_obj.normaluser.department=models.Department.objects.get(main_id=department_id)
                user_obj.save()
                messages.success(request,'User created successfully !')
                return HttpResponseRedirect(reverse('signup'))
            except:
                messages.error(request,'User registration falied as user already exists !')
                return HttpResponseRedirect(reverse('signup'))
