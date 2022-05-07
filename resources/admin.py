from django.contrib import admin
from django.contrib.gis import admin
from .models import CoffeeTypes, Shop, Street, County
# Register your models here.


@admin.register(CoffeeTypes)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.OSMGeoAdmin):
    pass


@admin.register(Street)
class StreetAdmin(admin.OSMGeoAdmin):
    pass


@admin.register(County)
class CountyAdmin(admin.OSMGeoAdmin):
    pass
