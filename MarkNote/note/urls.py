from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.post_list,name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>",views.post_detail,name="post_detail"),
    path("create-post/",views.create_post,name="createpost"),
    path("my_post/",views.show_my_post,name="my_post"),
]
