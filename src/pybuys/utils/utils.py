from product.models import Categorias, Productos

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

    