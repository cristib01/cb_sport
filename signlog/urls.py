from django.urls import path
from .views import *

app_name = 'signlog'
urlpatterns = [
    path('', index, name='index'),
    path('inregistrare/', user_signup, name='signup'),
    path('logare/', user_login, name='login'),
    path('logare-o/', user_logout, name='logout'),
    path('despre-noi/', about, name='about'),
    path('produse/', products, name='products')
]
