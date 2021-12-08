from django.urls import path
from mainapp.views import products, ProductDetail

app_name = 'products'
urlpatterns = [

    path('', products, name='products'),
    path('detail/,int:pk>/', ProductDetail.as_view(), name='detail'),
]
