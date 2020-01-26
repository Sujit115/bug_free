from django.shortcuts import render
from listing.choices import price_choices, bedroom_choices, state_choices
# Create your views here.

from listing.models import Listing

def index(request):
    listings = Listing.objects.order_by('list_date')

    context = {
        
        'listings' : listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices

    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

