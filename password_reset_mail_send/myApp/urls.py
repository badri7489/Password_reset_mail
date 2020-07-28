from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoggedPage, name='hogaya'),
    path('login/', views.LoginPage, name='login'),
    path('password_reset/', views.pass_reset, name='reset'),
    path('mail_sent/', views.pass_reset_mail_sent, name='sent'),
    path('new_pass/', views.pass_new, name='new'),
]
