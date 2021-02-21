from django.shortcuts import render
from django.http import HttpResponse

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
