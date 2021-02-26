from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser, Normaluser
from django.contrib import messages

def render_user_dashboard(request):
    profile_image =  request.user.normaluser.profile_image
    image1 = '../../../media/'+str(profile_image)
    context = {'image': image1}
    return render(request, "user_templates/user_dashboard.html",context)

def render_user_profile(request):
    profile_image =  request.user.normaluser.profile_image
    image1 = '../../../media/'+str(profile_image)
    context = {'image': image1}
    return render(request, "user_templates/user_profile.html",context)

def perform_user_profile(request):
    main_id = request.POST.get("main_id")
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    username = request.POST.get("username")
    email = request.POST.get("email")
    employee_number = request.POST.get("employee_number")
    mobile_number = request.POST.get("mobile_number")
    print(email)
    try:
        print("User Updation Initiated")
        user_obj = Normaluser.objects.get(main_id=main_id)
        user_obj.user.first_name = firstname
        user_obj.user.last_name = lastname
        user_obj.user.username = username
        user_obj.user.email = email
        user_obj.user.employee_number = employee_number
        user_obj.mobile_number = mobile_number
        user_obj.save()
        print(user_obj)
        messages.success(request, "Your profile was updated successfully !")
        return HttpResponseRedirect("user_profile")
        
    except:
        messages.error(request, "Failed to update your profile !")
        return HttpResponseRedirect("user_profile")
        

