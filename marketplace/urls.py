from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from  .forms import LoginForm

app_name = 'marketplace'

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('contact-us/', views.contactView, name='contact-us'),
    path('about-us/', views.AboutPageView, name='about-us'),
    path('signup/', views.signUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form = LoginForm), name='login'),
]