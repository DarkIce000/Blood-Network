from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User 

@login_required(login_url="login_view")
def index(request):   
    return render(request, "homepage/index.html", {
        "message": "Homepage"
    })


def blood_info_page_view(request):
    return render(request, "homepage/blood_info_page.html", {
        "message": "Homepage"
    })
    pass 


def order_page_view(request):
    return render(request, "homepage/order_page.html", {
        "message": "Homepage"
    })


def add_blood_view(request):
    return render(request, "homepage/add_blood.html", {
        "message": "Homepage"
    })

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not  None:
            login(request, user)
            return HttpResponseRedirect(reverse("index_page_view"))
        else:
            return render(request, "homepage/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "homepage/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_view"))


def register_view(request):
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        contact_no = request.POST["contact"]
        address = request.POST["address"]
        user_type = request.POST["user_type"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["cnfpassword"]
        if password != confirmation:
            return render(request, "mail/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username, 
                email=email, 
                contact_no=contact_no, 
                address=address, 
                user_type=user_type
                )
            
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "homepage/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index_page_view"))
    else:
        return render(request, "homepage/register.html")
