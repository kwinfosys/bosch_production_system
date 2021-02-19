from django.shortcuts import render
from django.http import HttpResponse

def render_admin_dashboard(request):
    return render(request, "admin_templates/admin_dashboard.html")
