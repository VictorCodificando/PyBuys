from django.shortcuts import get_object_or_404, redirect, render

from buysSales.models import Compras, ProductosEnCarrito, Ventas
from product.models import Productos
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

def shopping_cart(request):
    if request.method == 'POST':
        carrito_usuario = ProductosEnCarrito.objects.filter(id_usuario=request.user.id)
        productos_carrito = [(producto.producto, producto.cantidad) for producto in carrito_usuario]
        if productos_carrito == []:
            messages.error(request, "No hay productos en el carrito.")
            return redirect('shopping_cart')
        with transaction.atomic():
            for producto, cantidad in productos_carrito:
                # Verificar si hay suficiente cantidad en el inventario
                if producto.cantidad < cantidad:
                    messages.error(request, f"No hay suficiente cantidad de {producto.nombre} en el inventario.")
                    return redirect('shopping_cart')

            for producto, cantidad in productos_carrito:
                # Crear un nuevo registro de compra
                venta = Ventas(
                    id_usuario=request.user,
                    id_producto=producto,
                    cantidad=cantidad,
                )
                venta.save()

                # Actualizar la cantidad de producto en el inventario
                producto.cantidad -= cantidad
                producto.save()

                # Eliminar producto del carrito
                carrito_usuario.filter(producto=producto).delete()

            messages.success(request, "Compra realizada con éxito.")
            return redirect('shopping_cart')

    else:
        carrito_usuario = ProductosEnCarrito.objects.filter(id_usuario=request.user.id)
        productos_carrito = [(producto.producto, producto.cantidad) for producto in carrito_usuario]

        return render(request, "buysSales/shopping_cart.html", {"productos": productos_carrito})



def buy(request):
    return render(request, "buysSales/buys.html")

from django.http import JsonResponse

def add_to_cart(request, id_producto):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        try:
            cantidad = int(cantidad)
        except (ValueError, TypeError):
            return JsonResponse({'error': "La cantidad proporcionada no es válida."}, status=400)

        producto = get_object_or_404(Productos, id=id_producto)

        if producto.cantidad < cantidad:
            return JsonResponse({'error': f"No hay suficiente cantidad de {producto.nombre} en el inventario."}, status=400)

        carrito, created = ProductosEnCarrito.objects.get_or_create(id_usuario=request.user, producto=producto, defaults={'cantidad': cantidad})

        if not created:
            if producto.cantidad < (carrito.cantidad + cantidad):
                return JsonResponse({'error': f"No hay suficiente cantidad de {producto.nombre} en el inventario para añadir más al carrito."}, status=400)

            carrito.cantidad += cantidad
            carrito.save()

        return JsonResponse({'success': "Producto añadido al carrito con éxito."})

