from django.urls import path
from . import views

app_name = 'sports'
urlpatterns = [
    path('', views.sports, name='all_sports'),
    path('detaliu/<int:pk>/', views.sport_detail, name='sport_detail'),
    path('adauga-sport/', views.sport_add, name='add')
]
