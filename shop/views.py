from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def t_list(request):
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'shop/product/list.html'
    context = {
        'products': products,
        'page': page
    }
    return render(request, template ,context)


def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    template = 'shop/product/list.html'
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'page': page
    }
    return render(request, template, context)


def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render_to_response('shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})



