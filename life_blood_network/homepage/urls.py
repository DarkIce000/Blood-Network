from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("order", views.index, name="order")
]