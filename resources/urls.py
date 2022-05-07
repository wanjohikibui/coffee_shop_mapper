from django.urls import path
from .views import ShopAPI

urlpatterns = [
    path('shop/api', ShopAPI.as_view(), name='shop_api')
]
