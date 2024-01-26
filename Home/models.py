from django.db import models


# Create your models here:
class Schedule(models.Model):
    flight_ID = models.CharField(max_length=10, default='B8700')
    departure_Time = models.TimeField()
    landing_Time = models.TimeField()

    def __str__(self):
        return self.flight_ID


class Airport(models.Model):
    airport_ID = models.AutoField(primary_key=True)
    airport_Name = models.CharField(max_length=40, default='Hazrat Shahjalal International Airport')
    area = models.CharField(max_length=40, default='Dhaka') # same as departure place

    def __str__(self):
        return self.airport_Name


class FlightInfo(models.Model):
    flight_Image = models.ImageField(upload_to='Airlines/Images')
    flight_ID = models.CharField(max_length=10, default='B8700')
    flight_Name = models.CharField(max_length=40)
    flight_Class = models.CharField(max_length=10, default='Economy')
    flight_Price = models.FloatField()
    departure_Place = models.CharField(max_length=40, default='Dhaka')
    destination = models.CharField(max_length=40)

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, blank=True, null=True)

    # blank = True -> dileo hobe nadileo hobe. reverse of 'required' in forms;
    # null = True -> stores empty value;

    def __str__(self):
        return self.flight_Name


class Purchase(models.Model):
    customer_ID = models.AutoField(primary_key=True)
    customer_Name = models.CharField(max_length=40)
    customer_Email = models.EmailField()
    customer_Address = models.TextField()
    customer_Phone = models.CharField(max_length=14, default="+880")

    def __str__(self):
        return self.customer_Name