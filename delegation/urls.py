
from django.urls import path
from delegation import views
urlpatterns = [
    path("",views.home, name='index'),
    path("zz/",views.check,name='zz'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup')
]