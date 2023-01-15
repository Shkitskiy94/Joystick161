from django.urls import path

from .views import Home, SubCategoryHome, ProductHome

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('<slug:category_slug>/', SubCategoryHome.as_view(), name='subcategory'),
    # path('/<slug:subcategory_slug>/', SubCategoryHome.as_view(), name='subcategory'),
    path('product/<slug:product_slug>', ProductHome.as_view(), name='product'),
]
