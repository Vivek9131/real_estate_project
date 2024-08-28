from django.shortcuts import render

def home_page(request):
    return render(request , 'home_page.html')

def dream_house_page(request):
    return render(request , 'dream_house_page.html')

def view_property_page(request):
    return render(request , 'view_property_page.html')

def contact_us(request):
    return render(request , 'contact_us_page.html')