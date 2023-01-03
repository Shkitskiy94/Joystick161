from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoryHome.as_view(), name='category'),
]
