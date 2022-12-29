from django.views.generic import ListView

from .models import *


class CategoryHome(ListView):
    model = Category
    template_name = 'store/index.html'

class SubCategoryHome(ListView):
    model = SubCategory
    template_name = 'store/index.html'
    paginate_by = 5


class ProductHome(ListView):
    model = Product
    template_name = 'store/index.html'
    paginate_by = 10
