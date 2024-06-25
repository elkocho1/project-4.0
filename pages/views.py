from django.shortcuts import render

# Create your views here.

def index_views(request):
    return render(request, 'core/index.html')

def contact_views(request):
    return render(request, 'core/contact.html')