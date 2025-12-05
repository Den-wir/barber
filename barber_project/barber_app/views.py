from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    
    return render(request, 'home.html')   

def catalog(request):
    services = Service.objects.all()
    return render(request, 'catalog.html', {'services': services})  

def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'book_service.html', {'service': service})