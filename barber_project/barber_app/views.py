from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    
    return render(request, 'home.html')   

def catalog(request):
    
    return render(request, 'catalog.html')   