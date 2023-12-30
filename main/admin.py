from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from . import models



@admin.register(models.User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ( 'phone_number', 'age', 'state', 'region', 'address_street', 'sex', 'nationlity', 'password_series','status' )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )



admin.site.register(models.Sponsors)
admin.site.register(models.Service)
admin.site.register(models.Image)
admin.site.register(models.Hotel)
admin.site.register(models.Category_address)
admin.site.register(models.Sub_category_address)
admin.site.register(models.Room_Image)
admin.site.register(models.Room)
admin.site.register(models.Order_room)
admin.site.register(models.Achievement)
admin.site.register(models.Hotel_food)
admin.site.register(models.Order_hotel_food)
admin.site.register(models.Porkofka)
admin.site.register(models.Order_porkofka)
admin.site.register(models.Git)
admin.site.register(models.Order_restaran_food)
admin.site.register(models.Employee)
admin.site.register(models.Restaran)
admin.site.register(models.Table)
admin.site.register(models.Restaran_room)
admin.site.register(models.Order)
admin.site.register(models.Employee_restaran)
admin.site.register(models.Mean)
admin.site.register(models.Category)
admin.site.register(models.Sub_category)
admin.site.register(models.Languge)
