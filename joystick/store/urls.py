from django.urls import path

from .views import CategoryHome, ProductHome

urlpatterns = [
    path('', CategoryHome.as_view(), name='category'),
    path('product/<slug:product_slug>', ProductHome.as_view(), name='product'),
]
