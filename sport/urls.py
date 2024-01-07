from django.urls import path
from . import views

# app_name = 'sports'
# urlpatterns = [
#     path('', views.sports, name='all_sports'),
#     path('<int:sport_id>/', views.sport_detail, name='sport_detail'),
#     path('sports/', views.sport_add, name='add')
# ]

app_name = 'sports'
urlpatterns = [
    path('', views.SportsView.as_view(), name='all_sports'),
    path('detaliu/<int:pk>/', views.SportDetailView.as_view(), name='sport_detail'),
    path('sport/', views.SportCreateView.as_view(), name='add')
]
