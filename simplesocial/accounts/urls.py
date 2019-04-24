from django.urls import path, include
from django.contrib.auth import views as auth_views # For login logout
from . import views # for my views rendering works

app_name = 'accounts'

# Login and Logout views are inbuilt and we have to make Signup views only

urlpatterns = [
    # For login view we needed to connect to a template, and logout view has default
    path('login/',auth_views.LoginView.as_view(template_name=
         'accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]
