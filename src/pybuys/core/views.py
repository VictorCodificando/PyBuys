from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from core.forms import SignUpForm
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
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Validar si el correo electrónico ya está registrado en la base de datos
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Este correo electrónico ya está registrado.')
            else:
                form.save()
                return redirect("/login")
    else:
        form = SignUpForm()
    return render(request, "core/signup.html", {"form": form})


@login_required
def index(request):
    productos = Productos.objects.filter(cantidad__gt=0).order_by("-creado")[:16]
    return render(
        request,
        "core/index.html",
        {
            "grupo": None,
            "productos": productos,
            "titulo": "Inicio",
            "header": "Últimos productos",
        },
    )


@login_required
def logout(request):
    request.session.flush()
    return redirect("home")
