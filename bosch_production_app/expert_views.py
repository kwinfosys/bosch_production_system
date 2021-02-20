from django.shortcuts import render
from django.http import HttpResponse

def render_expert_dashboard(request):
    return render(request, "expert_templates/expert_dashboard.html")

def render_expert_profile(request):
    return render(request, "expert_templates/expert_profile.html")
