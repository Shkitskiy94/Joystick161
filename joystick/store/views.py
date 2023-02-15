from django.views.generic import ListView, DetailView, CreateView
# from django.views.generic.edit import FormMixin
from cart.forms import CartAddProductForm
from .models import *
from .form import ReviewForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class Home(ListView):
    model = Category
    template_name = 'store/index.html'
    context_object_name = 'category'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.all()
        context['product'] = Product.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        context['cat_selected'] = 0
        return context


class SubCategoryHome(ListView):
    model = SubCategory
    template_name = 'store/subcategory.html'
    context_object_name = 'subcategory'
    allow_empty = True

    def get_queryset(self):
        return SubCategory.objects.filter(category__slug=self.kwargs['category_slug'])
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['product'] = Product.objects.all()
        # context['cat_selected'] = context['subcategory'][0].category_id
        return context


class StoreHome(ListView):
    model = Product
    template_name = 'store/store.html'
    context_object_name = 'store'
    allow_empty = True

    def get_queryset(self):
        return Product.objects.filter(subCategory__slug=self.kwargs['subCategory_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['subcategory'] = SubCategory.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        return context


class ProductHome(DetailView, CreateView):
    model = Product
    form_class = ReviewForm
    template_name = 'store/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = Product.objects.filter(subCategory__title=self.kwargs['product_slug'])
        context['category'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        context['review'] = Review.objects.filter(product__slug=self.kwargs['product_slug'])
        return context  
    

    # def form_valid(self, form):
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.author = self.request.user
    #         comment.product = self.request.product
    #         comment.save()

    def form_valid(self, form):
        review = form.save(commit=False)
        review.save()
        return HttpResponseRedirect(reverse('store:home'))