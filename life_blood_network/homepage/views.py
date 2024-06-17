from django.forms import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import *
from .forms import *
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



def index(request):
    # uncomment it for adding data to db 
    # addDB()
    list = bloodStock.objects.all()
    return render(request, "homepage/index.html", {
        "message": "Homepage",
        "list": list 
    })
    
@csrf_exempt
def approval(request):
    get_user = User.objects.get(username=request.user)
    get_orders = order.objects.filter(blood_details__blood_bank=get_user)

    if request.method == "PUT":
        user_input = json.loads(request.body)
        if user_input.get("status") is not None:
            get_objects = order.objects.get(id=user_input["id"])

            if user_input["status"] == "approve":
                get_objects.approve_status = True
            else:
                get_objects.rejected_status = True

            get_objects.save()
        
        return JsonResponse([order.serialize() for order in get_orders], safe=False) 

    if request.method == "DATA":
        return JsonResponse([order.serialize() for order in get_orders], safe=False) 
    
    return render(request, "homepage/approval.html")
     



def blood_info(request, listing_id):
    try:
        get_details = bloodStock.objects.get(id=listing_id)    
    except:
        get_details = ""
    order_form = orderForm

    if request.method == "POST":
        post = request.POST.copy()
        user = User.objects.get(username=request.user)
        order_form_post = order_form(request.POST, request.FILES)

        if order_form_post.is_valid():
            order_instance = order_form_post.save(commit=False)
            order_instance.user = user
            order_instance.blood_details = get_details
            order_instance.save()
            return HttpResponseRedirect(reverse("my_orders_view"))

        return HttpResponse(f'form not saved succesfully ')
        

    return render(request, "homepage/blood_info_page.html", {
        "blood_details": get_details, 
        "order_form": order_form
    })


def search(request):
    search_result = bloodStock.objects.filter(blood_bank__address__icontains=f'{request.GET["query"]}')

    if not search_result:
        return render(request, "homepage/index.html", {
            "list": search_result,
            "value": request.GET["query"]
        })

    return render(request, "homepage/index.html", {
        "list": search_result, 
        "value": request.GET["query"]
    })


@login_required(login_url="login_view")
def my_profile(request):

    user = User.objects.get(username=request.user) 
    form = ProfilePageForm(instance=user)
    formtosave= ProfilePageForm(request.POST, files=request.FILES, instance=user)

    if request.method == "POST":
        if formtosave.is_valid():
            formtosave.save()
        else:
            return HttpResponse(f'profile not valid')
        
        return HttpResponseRedirect(reverse('my_profile_view')) 

    profile_img = None if not user.profile_img else user.profile_img

    return render(request, "homepage/profile.html", {
        "form": form,
        "profile_img": profile_img
    })


@login_required(login_url="login_view")
def my_order(request):
    get_user = User.objects.get(username=request.user)
    get_approved_orders = order.objects.filter(user=get_user, approve_status=True) 
    get_rejected_orders = order.objects.filter(user=get_user, rejected_status=True) 
    get_cancelled_orders = order.objects.filter(user=get_user, cancel_status=True) 
    get_pending_orders = order.objects.filter(user=get_user, approve_status=False, cancel_status=False, rejected_status=False) 
    return render(request, "homepage/order_page.html", {
        "pending_orders": get_pending_orders,
        "approved_orders": get_approved_orders, 
        "cancelled_orders": get_cancelled_orders,
        "rejected_orders": get_rejected_orders
    })


@login_required(login_url="login_view")
def add_blood(request):

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
        
        return HttpResponseRedirect(reverse('index_view'))

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
            return HttpResponseRedirect(reverse("index_view"))
        else:
            return render(request, "homepage/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "homepage/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_view"))


def register(request):
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
