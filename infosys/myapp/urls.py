from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    
   path("login/",views.index,name='login'),
   path("",views.registration,name='home'),
   path("dashboard/",views.dashboard,name='dashboard'),
   path("__reload__/", include("django_browser_reload.urls")),
]
