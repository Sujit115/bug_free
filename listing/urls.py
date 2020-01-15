from django.urls import path
from . import views

app_name = "listing"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:listing>', views.listing, name="listing"),
    path('search/', views.search, name="search")
]
