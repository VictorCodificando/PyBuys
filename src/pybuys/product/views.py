from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django import template

import json
from product.models import Categorias, Productos
import utils


@login_required
def product_detail(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    return render(request, "product/detail.html", {"producto": producto})

@login_required
def productos(request):
    query = request.GET.get("query", "").strip()
    id_categoria = int(request.GET.get("categoria", 0))
    if not request.user.is_staff:
        productos = Productos.objects.filter(cantidad__gt=0).order_by("-creado")
    else:
        productos = Productos.objects.order_by("-creado")
    titulo = ""
    header = ""
    if id_categoria:
        productos = list(
            filter(
                lambda producto: utils.pertenece_a_categoria(
                    producto.categoria, Categorias.objects.get(pk=id_categoria)
                ),
                productos,
            )
        )
        titulo = Categorias.objects.get(pk=id_categoria).nombre
        header = titulo

    elif query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
        titulo = "Busqueda"
        header = f"Resultados de la busqueda <<{query}>>"
    else:
        return redirect(request, "index")
    return render(
        request,
        "core/index.html",
        {
            "productos": productos[:16],
            "query": query,
            "grupo": id_categoria,
            "titulo": titulo,
            "header": header,
        },
    )

@login_required
def buscar_productos(request):
    query = request.GET.get("query", "")
    productos = Productos.objects.filter(
        Q(nombre__icontains=query)
    )[:10].values('nombre')
    productos_list = [p['nombre'] for p in productos]
    productos_json = json.dumps(productos_list)
    return HttpResponse(productos_json, content_type='application/json')
