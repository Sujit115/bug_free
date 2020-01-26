from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
from .choices import state_choices, bedroom_choices, price_choices

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

    listings = None
    if 'keywords' in request.GET:
        search_phrase = request.GET.get('keywords')
        if search_phrase: 
            listings = Listing.objects.filter(title__icontains = search_phrase)

    context = {
        
        'listings' : listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices

    }

    return render(request, 'listing/search.html', context)









    