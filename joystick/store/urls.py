from django.urls import path

from .views import *

urlpatterns = [
    path('', SubCategoryHome.as_view(), name='home'),
]
