from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("contact/",views.Contact, name="contact"),
    path("register/",views.Register, name="register"),
    path("products/<slug>/",views.Product, name="products"),
    path("single/<int:pk>/",views.Single, name="single"),
]
