from django.shortcuts import render

# Create your views here.

from listing.models import Listing

def index(request):
    listings = Listing.objects.order_by('list_date')

    context = {
        'listings' : listings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

