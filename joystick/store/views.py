from django.views.generic import ListView, DetailView

from .models import *


class CategoryHome(ListView):
    model = Category
    template_name = 'store/index.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.all()
        context['product'] = Product.objects.all()
        context['cat_selected'] = 0
        return context



class ProductHome(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = Product.objects.all()
        context['category'] = Category.objects.all()
        return context

