from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pybuys.settings import MEDIA_URL

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def login(request):
    if(request.user.is_authenticated):
        index(request)
    return render(request, "core/login.html")


def signup(request):
    if(request.user.is_authenticated):
        index(request)
    return render(request, "core/signup.html")


@login_required
def index(request):
    return render(request, "core/index.html")
