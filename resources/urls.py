from django.urls import path
from .views import ShopAPI, HomeView

urlpatterns = [
    path('shop/api', ShopAPI.as_view(), name='shop_api'),
    path('', HomeView.as_view(), name='home')
]
