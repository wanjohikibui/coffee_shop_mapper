from django.contrib import admin
from django.contrib.gis import admin
from .models import CoffeeTypes, Shop, Street, County
from leaflet.admin import LeafletGeoAdmin
# Register your models here.


@admin.register(CoffeeTypes)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(LeafletGeoAdmin):
    pass


@admin.register(Street)
class StreetAdmin(LeafletGeoAdmin):
    pass


@admin.register(County)
class CountyAdmin(LeafletGeoAdmin):
    pass
