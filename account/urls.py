from django.urls import path
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', csrf_protect(auth_views.LogoutView.as_view()), name='logout'),
]