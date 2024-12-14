from django.urls import path
from django.urls import include
from registro.views import signupView, home 


urlpatterns = [ 
    path("accounts/",include('django.contrib.auth.urls')),
    path("singnup/", signupView.as_view(), name="signup"),
    path("",home,name = "home"),



]
