from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Estilos para los campos de los formularios
field_attrs = {
    "class": "w-full py-4 px-6 rounded-xl mt-4 bg-gray-200",
    "placeholder": "",
}


# Formulario de inicio de sesión
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                **field_attrs,
                "placeholder": "Nombre de usuario",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                **field_attrs,
                "placeholder": "Contraseña",
            }
        )
    )


# Formulario de registro de usuarios
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                **field_attrs,
                "placeholder": "Nombre de usuario",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                **field_attrs,
                "placeholder": "Correo electrónico",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                **field_attrs,
                "placeholder": "Contraseña",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                **field_attrs,
                "placeholder": "Repetir contraseña",
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# Formulario para cambiar la usuario y/o correo electrónico
class ChangeUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                **field_attrs,
                "placeholder": "Nombre de usuario",
            }
        )
    )
    
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                **field_attrs,
                "placeholder": "Correo electrónico",
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "email")
        

    def __init__(self, *args, **kwargs):
        super(ChangeUserForm, self).__init__(*args, **kwargs)

