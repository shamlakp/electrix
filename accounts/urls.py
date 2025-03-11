from django.urls import path
from .views import admin_login, admin_register, dashboard

urlpatterns = [
    path("admin_login/",admin_login, name="admin_login"),
    path("register/", admin_register, name="admin_register"),
    path("dashboard/",dashboard, name="dashboard"),
  
]
