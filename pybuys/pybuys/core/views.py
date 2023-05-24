from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from core.forms import ChangeUserForm, SignUpForm
from product.models import Productos
from pybuys.settings import MEDIA_URL
from utils.utils import modificarUsuario



def home(request):
    if request.user.is_authenticated:
        return redirect("/index")
    return render(request, "core/home.html")


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
    if not request.user.is_staff:
        productos = Productos.objects.filter(cantidad__gt=0).order_by("-creado")[:16]
    else:
        productos = Productos.objects.order_by("-creado")[:16]
        
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

@login_required
def configuracion_usuario(request):
    if request.method == "POST":
        form = ChangeUserForm(request.POST)
        if form.is_valid():
            # Validar si el correo electrónico ya está registrado en la base de datos
            email = form.cleaned_data.get('email')
            username=form.cleaned_data.get('username')
            if User.objects.filter(email=email).exclude(username=request.user.username).exists():
                form.add_error('email', 'Este correo electrónico ya está registrado.')
            elif User.objects.filter(username=username).exclude(email=request.user.email).exists():
                form.add_error('username', 'Este nombre de usuario ya está registrado.')
            else:
                modificarUsuario(request.user.username, form.cleaned_data.get('username'), form.cleaned_data.get('email'))
                messages.success(request, "Usuario modificado con éxito.")
                return redirect("/index")
    else:
        form = ChangeUserForm()
    return render(request, "core/configuracion_usuario.html", {"form": form})
