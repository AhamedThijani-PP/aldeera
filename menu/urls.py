from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="home"),
    path('menu/', views.menu,name="menu"),
    path('menu/<str:slug>/',views.menu,name="menu")
]