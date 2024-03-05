from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request, "homepage/index.html", {
        "message": "Homepage"
    })