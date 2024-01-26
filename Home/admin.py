from django.contrib import admin
from Home.models import FlightInfo, Schedule, Airport, Purchase


# Register your models here.
admin.site.register(FlightInfo)
admin.site.register(Schedule)
admin.site.register(Airport)
admin.site.register(Purchase)