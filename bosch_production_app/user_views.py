from django.shortcuts import render
from django.http import HttpResponse

def render_user_dashboard(request):
    return render(request, "user_templates/user_dashboard.html")
