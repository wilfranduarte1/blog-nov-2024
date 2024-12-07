from django.urls import path
from django.urls import include


urlspatterns = [ 
    path("accounts/",include(django.contrib.auth.urls)),
    path("signup/", signupView.as_view(), name="signup"),



]
