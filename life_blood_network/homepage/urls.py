from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("", views.index, name="index_view"),
   path("my-orders", views.my_order, name="my_orders_view"),
   path("add-blood", views.add_blood, name="add_blood_view"),
   path("login", views.login_view, name="login_view"),
   path("register", views.register, name="register_view"),
   path("logout", views.logout_view, name="logout_view"),
   path("profile", views.my_profile, name="my_profile_view"),
   path("search", views.search, name="search_view"),
   path("approval", views.approval, name="approval_view"),
   path("<int:listing_id>", views.blood_info, name="blood_info_view")
]
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)