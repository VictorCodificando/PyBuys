from django.shortcuts import render

from pybuys.settings import MEDIA_URL

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html',{"MEDIA_URL": MEDIA_URL + "core/"})

def signup(request):
    return render(request, 'accounts/signup.html', {"MEDIA_URL": MEDIA_URL + "core/"})