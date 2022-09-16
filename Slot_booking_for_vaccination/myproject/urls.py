"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from slotbooking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display,name = "home"),
    path('userLogin/',views.userLogin,name="user"),
    path('adminLogin/',views.adminLogin,name="admin"),
    path('signup/',views.signup,name="signup"),
    path('hlogin/',views.hlogin,name="hlogin"),
    path('hsign/',views.hsign,name = "hsign"),
    path('save',views.hsign),
    path('slotbooking/',views.slotbooking,name = "slotbooking"),
    path('slotbooking/slots',views.slots,name="slots"),
    path('signup1/',views.signup,name="signup1"),
    path('login1/',views.signup,name="login1"),
    path('logout/',views.logoutuser,name = "logout"),
    path('slotbooking/success',views.success,name = "success"),
    # path('slotbooking/<slug:slug_val>/',views.hospital,name = "hospital"),
    # path("/patientlogin",)
]
