from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, 'home_module/index_page.html')

def contact_page(request):
    return render(request, 'home_module/contact_page.html')
