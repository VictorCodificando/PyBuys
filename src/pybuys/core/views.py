from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from product.models import Categorias, Productos

from pybuys.settings import MEDIA_URL

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect("/index")
    return render(request, "core/home.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("/index")
    return render(
        request,
        "core/login.html",
    )


def signup(request):
    if request.user.is_authenticated:
        return redirect("/index")
    return render(request, "core/signup.html")


@login_required
def index(request):
    productos = Productos.objects.filter(cantidad__gt=0)[:10]
    return render(
        request,
        "core/index.html",
        {
            "grupo": None,
            "productos": productos,
        },
    )


@login_required
def logout(request):
    request.session.flush()
    return render(request, "core/home.html")
