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
        return context



class ProductHome(DetailView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'product'
