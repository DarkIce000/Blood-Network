from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("", views.index, name="index_page_view"),
   path("my_orders", views.order_page_view, name="order_page_view"),
   path("blood_info_page", views.blood_info_page_view, name="blood_info_page_view"),
   path("add_blood", views.add_blood_view, name="add_blood_page_view"),
   path("login", views.login_view, name="login_view"),
   path("register", views.register_view, name="register_view"),
   path("logout", views.logout_view, name="logout_view"),
   path("profile", views.my_profile_view, name="my_profile"),
   path("search", views.search, name="search_page"),
   path("<int:listing_id>", views.blood_info_page_view, name="info_page")
]
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)