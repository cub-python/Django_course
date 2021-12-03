from django.urls import path
# from authapp.views import
from authapp.views import login,register,logout

app_name = 'authapp'
urlpatterns = [

    path('login/', register, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
