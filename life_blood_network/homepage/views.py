from django.db import IntegrityError
from django.forms import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User, bloodStock, order
from .forms import ProfilePageForm, BloodStockForm, RegistrationForm
import json

def addDB():
    file = open('/home/darkice/bloodData (3rd copy).json', 'r')
    data = json.load(file)
    for j, i in enumerate(data['data']):
        new_user =  User.objects.create_user(f'bloodBank{j}', f'bloodBank{j}@gmail.com', password="1523@Lope")
        new_user.first_name = i[1]
        new_user.address = i[2]
        new_user.contact_no = i[3]
        new_user.user_type = "provider"
        new_user.save()

        for key, value in i[5].items():
            bd = bloodStock(blood_bank=new_user, blood_type=key, quantity=value) 
            bd.save() 



# @login_required(login_url="login_view")
# @addDB()
def index(request):
    # uncomment it to refresh db
    # addDB()
    list = bloodStock.objects.all()
    return render(request, "homepage/index.html", {
        "message": "Homepage",
        "list": list 
    })


def blood_info_page_view(request, listing_id):
    try:
        get_details = bloodStock.objects.get(id=listing_id)    
    except:
        get_details = ""

    if request.method == "POST":

        return HttpResponse(f'query group')

    return render(request, "homepage/blood_info_page.html", {
        "blood_details": get_details
    })


def search(request):
    search_result = bloodStock.objects.filter(blood_bank__address__icontains=f'{request.GET["query"]}')

    if not search_result:
        return render(request, "homepage/index.html", {
            "list": search_result
        })

    return render(request, "homepage/index.html", {
        "list": search_result
    })


@login_required(login_url="login_view")
def my_profile_view(request):

    user = User.objects.get(username=request.user) 
    form = ProfilePageForm(instance=user)
    formtosave= ProfilePageForm(request.POST, files=request.FILES, instance=user)

    if request.method == "POST":
        if formtosave.is_valid():
            formtosave.save()
        else:
            return HttpResponse(f'profile not valid')
        
        return HttpResponseRedirect(reverse('my_profile')) 

    profile_img = None if not user.profile_img else user.profile_img

    return render(request, "homepage/profile.html", {
        "form": form,
        "profile_img": profile_img
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
    add_blood_form = BloodStockForm

    if request.method == "POST":

        try:
            blood_stock = bloodStock.objects.get(blood_bank=blood_bank, blood_type=request.POST['blood_type'])
        except:
            blood_stock = bloodStock(blood_bank=blood_bank)

        new_value = request.POST.copy()
        new_value['quantity'] = int(new_value['quantity'])+int(blood_stock.quantity)
        add_blood = add_blood_form(new_value, instance=blood_stock)

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



# loging handling functions 
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
        user = RegistrationForm(request.POST, request.FILES)
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
