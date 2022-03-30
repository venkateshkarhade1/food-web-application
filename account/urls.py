from re import template
from django.contrib import admin
from django.urls import path ,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('signup',views.register, name="signup"),
    path('signin',views.login,name="signin"),
    path('logout',views.logout,name="logout"),
    path('delUser',views.delUser,name="delUser"),
    path('forget_password/',views.forget_password,name="forget_password"),
   # path('change_password/<slug:uid>/',views.change_password,name="change_password"),
    path('forget_password_done',views.forget_password_done,name="forget_password_done"),
    
]
