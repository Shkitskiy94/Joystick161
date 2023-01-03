from django.views.generic import ListView

from .models import *


class CategoryHome(ListView):
    model = Category
    template_name = 'includes/header.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.filter('title')
        return context



class SubCategoryHome(ListView):
    model = SubCategory
    template_name = 'store/index.html'
    context_object_name = 'subcategory'


class ProductHome(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'product'
