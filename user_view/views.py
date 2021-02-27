from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html', context=None)

def about(request):
    return render(request, 'about.html', context=None)

def contact(request):
    return render(request, 'contact.html', context=None)

def services(request):
    return render(request, 'services.html', context=None)
