from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Home.models import *


# Create your views here.
def index(request):

    return render(request, 'Home/Home.html')



def flights(request):

    obj = FlightInfo.objects.all()
    dic = {'key': obj}

    return render(request, 'Home/HomePage.html', dic)



def about(request):

    return render(request, 'Home/About.html')



def cusBook(request):

    if request.method == 'POST':
        name = request.POST.get('customerName')
        email = request.POST.get('email')
        address = request.POST.get('Address')
        phone = request.POST.get('customerPhone')
        obj = Purchase(customer_Name=name, customer_Email=email, customer_Address=address, customer_Phone=phone)
        obj.save()

    return render(request, 'Customer/CustomerBook.html')


# Search:

def search(request):

    query = request.GET['Search']

    if len(query) > 40 or len(query) == 0:
        obj = [] # object is empty.

    else:
        objFrom = FlightInfo.objects.filter(departure_Place__icontains=query)
        objDestination = FlightInfo.objects.filter(destination__icontains=query)
        obj = objFrom.union(objDestination).order_by('flight_Price')

    dic = {'key': obj, 'search': query}

    return render(request, 'Home/Search.html', dic)
    # return HttpResponseRedirect('Home/Search.html', dic)


# Filter functions:
def priceFilter(request, filter):

    if filter == 'lowHigh':
        obj = FlightInfo.objects.all().order_by('flight_Price')
    
    else:
        obj = FlightInfo.objects.all().order_by('flight_Price').reverse()

    dic = {'key': obj}

    return render(request, 'Home/HomePage.html', dic)



def nameFilter(request, filter):

    if filter == 'lowHigh':
        obj = FlightInfo.objects.all().order_by('flight_Name')

    else:
        obj = FlightInfo.objects.all().order_by('flight_Name').reverse()

    dic = {'key': obj}

    return render(request, 'Home/HomePage.html', dic)


# def searchFilterLow(request, search):
#     print(search)
#     return HttpResponse('<h1> {{search}} </h1> ')

def searchPriceFilter(request, search, filter):

    objFrom = FlightInfo.objects.filter(departure_Place__icontains=search)
    objDestination = FlightInfo.objects.filter(destination__icontains=search)

    if filter == 'lowHigh':
        obj = objFrom.union(objDestination).order_by('flight_Price')

    else:
        obj = objFrom.union(objDestination).order_by('flight_Price').reverse()

    dic = {'key': obj, 'search': search}

    return render(request, 'Home/Search.html', dic)


def searchNameFilter(request, search, filter):

    objFrom = FlightInfo.objects.filter(departure_Place__icontains=search)
    objDestination = FlightInfo.objects.filter(destination__icontains=search)

    if filter == 'AtoZ':
        obj = objFrom.union(objDestination).order_by('flight_Name')

    else:
        obj = objFrom.union(objDestination).order_by('flight_Name').reverse()

    dic = {'key': obj, 'search': search}

    return render(request, 'Home/Search.html', dic)