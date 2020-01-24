from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 1) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'listings' : page_obj
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









    