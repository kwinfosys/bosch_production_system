from django.urls import path
from . import views, admin_views, user_views, expert_views

urlpatterns = [
    path('',views.render_signin, name='signin'),
    path('signup/',views.render_signup, name='signup'),
    path('perform_signin',views.perform_signin, name='perform_signin'),
    path('perform_signout',views.perform_signout, name='perform_signout'),
    path('perform_signup',views.perform_signup, name='perform_signup'),

    # Admin Endpoints
    path('admin_dashboard/', admin_views.render_admin_dashboard, name="admin_dashboard"),

    # User Endpoints
    path('user_dashboard/', user_views.render_user_dashboard, name="user_dashboard"),
    path('user_profile/', user_views.render_user_profile, name="user_profile"),
    path('perform_user_profile', user_views.perform_user_profile, name="perform_user_profile"),
    
    # Expert Endpoints
    path('expert_dashboard/', expert_views.render_expert_dashboard, name="expert_dashboard"),
    path('expert_profile/', expert_views.render_expert_profile, name="expert_profile"),
]
