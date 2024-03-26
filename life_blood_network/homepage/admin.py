from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(bloodProvider)
admin.site.register(bloodReciever)
admin.site.register(bloodGroup)


