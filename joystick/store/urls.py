from django.urls import path

from .views import Home, SubCategoryHome, StoreHome, ProductHome

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<slug:category_slug>/', SubCategoryHome.as_view(), name='subcategory'),
    path('<slug:subCategory_slug>/', StoreHome.as_view(), name='store'),
    path('product/<slug:product_slug>', ProductHome.as_view(), name='product'),
]
