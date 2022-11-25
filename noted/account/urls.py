from django.contrib.auth.views import LoginView
from django.urls import path

from account import views


urlpatterns = [
    path("signup-request/", views.send_singup_email, name="signup_request"),
    path("validate-email/", views.validate_email, name="validate_email"),
    path("signup/<str:token>/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
]
