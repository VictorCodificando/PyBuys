from django.shortcuts import render

# Create your views here.

from django.shortcuts import render



def product_detail(request, pk):

    return render(request, "product/detail.html", {})


def product_new(request):
    return render(request, "product/new.html", {})


def product_edit(request, pk):
    return render(request, "product/edit.html", {})
