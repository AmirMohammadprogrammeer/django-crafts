from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("",views.form_register,name="register"),
    path("logout/",views.form_logout,name="logout"),
    path("login/",views.login_form,name="login"),
]   