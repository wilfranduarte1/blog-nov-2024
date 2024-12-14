from django.urls import path
from django.urls import include
from registro.views import signupView


urlpatterns = [ 
    path("accounts/",include('django.contrib.auth.urls')),
    path("", signupView.as_view(), name="signup"),



]
