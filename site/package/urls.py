from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name="home-page"),
    path("create/package/",views.create_package,name="create"),
    path("show_detail/",views.show_package,name="show"),
    path("detail/<int:id>/",views.detail_package,name="detail"),
    path("delete/<int:id>/",views.delete_package,name="del")
] 