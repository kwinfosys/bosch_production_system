from django.urls import path
from . import views, admin_views , user_views

urlpatterns = [
    path('',views.render_signin, name='signin'),
    path('signup/',views.render_signup, name='signup'),
    path('perform_signin',views.perform_signin, name='perform_signin'),
    path('perform_signup',views.perform_signup, name='perform_signup'),

    # Admin Endpoints
    path('admin_dashboard/', admin_views.render_admin_dashboard, name="admin_dashboard"),

    # User Endpoints
    path('user_dashboard/', user_views.render_user_dashboard, name="user_dashboard"),
]
