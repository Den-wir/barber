from django.urls import path
from . import views

app_name = 'barbershop'
    
urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('book/<int:service_id>/', views.book_service, name='book_service'),
]