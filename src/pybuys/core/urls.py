from django.urls import path

from django.contrib.auth import views as auth_views
from .forms import LoginForm, SignUpForm
from . import views

urlpatterns = [
    path('', views.home, name='home'),
        path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('configuration/', views.configuracion_usuario, name='configuration'),
]