from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('Fname','Lname','Email')

# class ShopAdmin(admin.ModelAdmin):
#     list_display = ('User','Shop_name','Shop_type')

admin.site.register(User,UserAdmin)
# admin.site.register(Shop, ShopAdmin)