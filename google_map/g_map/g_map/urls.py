from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/map', views.gmap,name='map'),
    #path('home/login',views.LoginPage,name='login'),


]