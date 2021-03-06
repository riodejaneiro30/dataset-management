from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import signup, logout_view

app_name = 'account'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup, name='signup')
]