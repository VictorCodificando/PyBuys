from product.models import Categorias, Productos
from django.contrib.auth.models import User

def pertenece_a_categoria(categoria_hijo, categoria):
    """
    Verifica si el producto o su grupo pertenece a una categoría determinada.
    """
    if categoria_hijo == categoria:
        return True
    elif categoria_hijo.grupo is None:
        return False
    else:
        # Si el producto tiene una categoría diferente, se revisa su grupo recursivamente
        return pertenece_a_categoria(categoria_hijo.grupo, categoria)

def modificarUsuario(oldusername, newusername, newemail):
    #Un print que diga lo que se va a hacer
    print("Se va a cambiar el nombre de usuario de " + oldusername + " a " + newusername + " y su correo electrónico a " + newemail)
    user = User.objects.get(username=oldusername)
    user.username = newusername
    user.email = newemail
    user.save()
    return user
    