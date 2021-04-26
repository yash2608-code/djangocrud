from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.FirstPage,name="firstpage"),
    path("second-page/",views.SecondPage,name="secondpage"),
    path("show-data/",views.ShowData,name="showdata"),
    path("update-page/<int:pk>/",views.UpdatePage,name="updatepage"),
    path("delete-user/<int:pk>/",views.DelUser,name="deluser"),
    path("reg-page/",views.RegPage,name="regpage"),
    path("reg-user/",views.RegUser,name = "reguser"),
    path("update-user/<int:pk>/",views.UpdateUser,name="updateuser"),
]