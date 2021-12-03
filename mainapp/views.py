from django.shortcuts import render

import json
import os

from mainapp.models import Product,ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geekshop | Каталог',
    }
    # context['products'] = json.load(open(file_path, encoding='utf-8'))
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)






# def test(request):
#     context = {
#         'title': 'geekshop',
#         'header': 'Добро пожаловать на сайт',
#         'user': 'Николай',
#         'products': [
#             {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6091},
#             {'name': 'Синяя куртка The North Face', 'price': 23726},
#             {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3391},
#             {'name': 'Черный рюкзак Nike Heritage', 'price': 2341},
#             {'name': 'Черные туфли на платформе с 4 парами люверсов Dr Martens 1461 Bex', 'price': 13590},
#             {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2891},
#         ],
#
#         'products_promo': [
#             {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 5001},
#             {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 2001},
#             {'name': 'Черный рюкзак Nike Heritage', 'price': 1001},
#
#         ]
#     }
#     return render(request, 'test_content.html', context)
