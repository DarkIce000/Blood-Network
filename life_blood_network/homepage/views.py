from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User 
from .forms import ProfilePageForm, BloodStockForm, RegistrationForm

@login_required(login_url="login_view")
def index(request):   
    return render(request, "homepage/index.html", {
        "message": "Homepage"
    })


def blood_info_page_view(request):
    return render(request, "homepage/blood_info_page.html", {
        "message": "Homepage"
    })
    

@login_required(login_url="login_view")
def my_profile_view(request):
    user = User.objects.get(username=request.user) 
    form = ProfilePageForm(instance=user)
    if request.method == "POST":
        formtosave= ProfilePageForm(request.POST)
        return HttpResponseRedirect(reverse('my_profile'))
    return render(request, "homepage/profile.html", {
        "form": form
    })

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
        # print(request.POST)
        # first_name = request.POST["first_name"]
        # last_name = request.POST["last_name"]
        # username = request.POST["username"]
        # email = request.POST["email"]
        # contact_no = request.POST["contact"]
        # address = request.POST["address"]
        # city = request.POST['city']
        # state = request.POST['state']
        # user_type = request.POST["user_type"]
        user = RegistrationForm(request.POST)
        
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if password != confirmation:
            return render(request, "mail/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            # user = User.objects.create_user(
            #     first_name=first_name,
            #     last_name=last_name,
            #     username=username, 
            #     email=email, 
            #     contact_no=contact_no, 
            #     city=city,
            #     state=state,
            #     address=address, 
            #     user_type=user_type
            #     )

            new_user = user.save(commit=False)
            new_user.password = makepassword(new_user.password)
        except IntegrityError as e:
            print(e)
            return render(request, "homepage/register.html", {
                "message": "Email address already taken."
            })
        
        login(request, new_user)
        return HttpResponseRedirect(reverse("index_page_view"))
    else:
        form = RegistrationForm()
        return render(request, "homepage/register.html", {
            "form": form
        })
