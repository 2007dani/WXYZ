"""WXYZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Translator import views


urlpatterns = [
    path('Translator/admin/', views.Admin_Page_Show),
    path('Translator/AddLanguage/<int:Amount>/',views.Add_Language),
    path('',views.Introduction),
    path('Translator/Login/',views.First_Page),
    path('Translator/Login/<Name>/<Password>',views.Check_Login, ) , 
    path('Translator/P2C/<Name>',views.GetP2C),
    path('Translator/C2P/<Name>',views.GetC2P) ,
    path('Translator/Result/C2P',views.GetResultC2P, name = "C2P"),
    path('Translator/Result/P2C',views.GetResultP2C , name = "P2C"),

]
