from django.shortcuts import render
from .models import Listing
# Create your views here.

def index(request):
    listings = Listing.objects.all()

    context = {
        'listings' : listings
    }

    return render(request, 'listing/listings.html', context)

def listing(request, listing_id):
    listing = Listing.objects.get(pk = listing_id)

    context = {
        'listing': listing
    }
    
    return render(request, 'listing/listing.html', context)

def search(request):
    return render(request, 'listing/search.html')