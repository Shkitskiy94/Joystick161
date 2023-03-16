from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Avg, Q, F, FloatField, ExpressionWrapper

from .form import ReviewForm
from .models import *


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
        context['top_discount'] = Product.objects.filter(
            discount_price__gt=0).annotate(discount_percent=ExpressionWrapper(
            100 - (F('discount_price') * 100 / F('price')),
            output_field=FloatField())).order_by('-discount_percent')[:10]
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
        context['cat_selected'] = context['subcategory'][0].category_id
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
        context['subcategory'] = Product.objects.filter(
            subCategory__title=self.kwargs['product_slug'])
        context['category'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        context['review'] = Review.objects.filter(product__slug=self.kwargs['product_slug'])
        context['avg_rating'] = Review.objects.filter(
            product__slug=self.kwargs['product_slug']
            ).aggregate(res=Avg('score')).get('res')
        return context

    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = self.request.user
        review.product = get_object_or_404(Product, pk=self.kwargs['product_slug'])
        review.save()
        return redirect(self.request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


class SearchHome(ListView):
    model = Product
    template_name = 'store/search.html'
    context_object_name = 'store'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_list = Product.objects.filter(
            Q(title__icontains=query) | Q(subCategory__title__icontains=query)
        )
        return search_list