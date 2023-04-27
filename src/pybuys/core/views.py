from django.shortcuts import render

from pybuys.settings import MEDIA_URL

# Create your views here.


def home(request):
    return render(request, "core/home.html", {"MEDIA_URL": MEDIA_URL + "/core/"})
