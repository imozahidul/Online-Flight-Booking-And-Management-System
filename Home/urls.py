from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('flights', views.flights),
    path('about', views.about),
    path('bookFlight', views.cusBook),
    path('search', views.search),

    # Filters:
    path('priceFilter/<filter>', views.priceFilter, name="priceFilter"),
    path('nameFilter/<filter>', views.nameFilter, name="nameFilter"),
    path('searchPriceFilter/<search>/<filter>', views.searchPriceFilter, name="searchPriceFilter"), # dynamic url; # name use kore function ta call hoy; tai path ekta dilei hoy; ei path kothao dewa nai;
    path('searchNameFilter/<search>/<filter>', views.searchNameFilter, name="searchNameFilter"), # dynamic url;
]