from django.db import IntegrityError
from django.forms import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User, bloodStock, order
from .forms import ProfilePageForm, BloodStockForm, RegistrationForm

@login_required(login_url="login_view")
def index(request):
    list = bloodStock.objects.all()
    for i in list: print(i)
    return render(request, "homepage/index.html", {
        "message": "Homepage",
        "list": list 
    })


def blood_info_page_view(request):
    if request.method == "POST":
        return HttpResponse(f'query group')
    return render(request, "homepage/blood_info_page.html", {
        "message": "Homepage"
    })
    

@login_required(login_url="login_view")
def my_profile_view(request):
    user = User.objects.get(username=request.user) 
    form = ProfilePageForm(instance=user)
    formtosave= ProfilePageForm(request.POST, instance=user)

    if request.method == "POST":
        if formtosave.is_valid():
            formtosave.save()
        else:
            return HttpResponse(f'profile not valid')
        
        return HttpResponseRedirect(reverse('my_profile')) 

    return render(request, "homepage/profile.html", {
        "form": form
    })


@login_required(login_url="login_view")
def order_page_view(request):
    return render(request, "homepage/order_page.html", {
        "message": "Homepage"
    })

@login_required(login_url="login_view")
def add_blood_view(request):
    blood_bank = User.objects.get(username=request.user) 
    # creating instance of the blood_stock 
    blood_stock = bloodStock(blood_bank=blood_bank)

    add_blood_form = BloodStockForm
    if request.method == "POST":
        print(request.POST)
        add_blood = add_blood_form(request.POST, instance=blood_stock )

        # form validity and usr_type is bloodbank
        if add_blood.is_valid():
            add_blood.save()
        else:
            return render(request, "homepage/add_blood.html", {
            "message": "some error in adding",
            'form':add_blood_form
            })
        
        return HttpResponseRedirect(reverse('index_page_view'))

    return render(request, "homepage/add_blood.html", {
        'form':add_blood_form
    })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
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
        user = RegistrationForm(request.POST)
        print('1')
        if user.is_valid(): 
            try:
                user.save()
            except ValidationError as error:
                return render(request, "homepage/register.html", {
                    "form": user,
                    'message': f'{error}'
                }) 
            return HttpResponseRedirect(reverse("login_view"))
        
        return render(request, "homepage/register.html", {
            "form": user,
            'message': 'Password Do not Match / Not as Specified'
        }) 

    form = RegistrationForm()
    return render(request, "homepage/register.html", {
        "form": form
    })
