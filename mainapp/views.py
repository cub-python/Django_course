from django.shortcuts import render

import json
import os
from django.views.generic import DetailView
from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)


def products(request,id_category=None,page = 1):

    context = {
        'title': 'Geekshop | Каталог',
    }

    if id_category:
        products = Product.objects.filter(category_id=id_category)

    else:
        products = Product.objects.all()
    paginator = Paginator(products,per_pape=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)


    context['products'] = products_paginator
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):  #контролер вывода информации о продукте

    model = Product
    template_name = 'mainapp/detail.html'

    # context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # Добваляем список категорий для вывода сайдбара с категориями на странице каталога
        context = super(ProductDetali, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context

