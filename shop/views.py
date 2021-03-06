from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def deliver(request):
    return render(request, 'other/delivery.html')


def contacts(request):
    return render(request, 'other/contacts.html')


def productlist(request, category_slug=None):
    template = 'shop/product/list.html'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    page = request.GET.get('page')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        sort_products = products.filter(category=category)
        paginator = Paginator(sort_products, 8)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        paginator = Paginator(products, 8)
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


def productdetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render_to_response('shop/product/detail.html',
                              {'product': product,
                               'cart_product_form': cart_product_form})
