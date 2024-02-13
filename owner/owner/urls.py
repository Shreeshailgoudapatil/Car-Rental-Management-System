"""owner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url("insertaddcustomer", views.insertaddcustomer, name="insertaddcustomer"),
    # url("insertlogin", views.insertlogin, name="insertlogin"),
    url("insertcomplaint", views.insertcomplaint, name="insertcomplaint"),
    url("insertcarbooking", views.insertcarbooking, name="insertcarbooking"),
    url("insertcardetails", views.insertcardetails, name="insertcardetails"),
    url("insertrentdetails", views.insertrentdetails, name="insertrentdetails"),
    url("insertadddriver", views.insertadddriver, name="insertadddriver"),
    url("inserttripchart", views.inserttripchart, name="inserttripchart"),

    url("viewlogin", views.viewlogin, name="viewlogin"),
    url('login_del/(?P<pk>\d+)/$', views.login_del, name='login_del'),

    url("viewcustomer", views.viewcustomer, name="viewcustomer"),
    url('customer_del/(?P<pk>\d+)/$', views.customer_del, name='customer_del'),

    url("viewadddriver", views.viewadddriver, name="viewadddriver"),
    url('driver_del/(?P<pk>\d+)/$', views.driver_del, name='driver_del'),

    url("viewtripchart", views.viewtripchart, name="viewtripchart"),
    url('tripchart_del/(?P<pk>\d+)/$', views.tripchart_del, name='tripchart_del'),

    url("viewcarbooking", views.viewcarbooking,name="viewcarbooking"),
    url("carbooking_del/(?P<pk>\d+)/$", views.carbooking_del, name='carbooking_del'),

    url("viewcardetails", views.viewcardetails,name="viewcardetails"),
    url("cardetails_del/(?P<pk>\d+)/$", views.cardetails_del, name='cardetails_del'),

    url("viewcomplaint", views.viewcomplaint,name="viewcomplaint"),
    url("compliaint_del/(?P<pk>\d+)/$", views.complaint_del, name='complaint_del'),

    url("viewrentdetails", views.viewrentdetails,name="viewrentdetails"),
    url("rentdetails_del/(?P<pk>\d+)/$", views.rentdetails_del, name='rentdetails_del'),

    url("adminhome", views.adminhome, name="adminhome"),
    url("logcheck", views.logcheck, name="logcheck"),

    url("^$", views.index, name="index"),

    url("index", views.index, name="index"),
    url("signin",views.signin,name="signin"),
    url("newuser",views.newuser,name="newuser"),
    url("sendpass", views.sendpass, name="sendpass"),
    url("user_home", views.user_home, name="user_home")
]
