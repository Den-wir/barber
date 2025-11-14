from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Barber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    is_active = models.BooleanField(default=True)

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class BarberService(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

class Schedule(models.Model):
    DAYS = [
        (1, 'Monday'),
        (2, 'Tuesday'), 
        (3, 'Wednesday'),
        (4, 'Thursday'), 
        (5, 'Friday'), 
        (6, 'Saturday'), 
        (7, 'Sunday')
    ]
    
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Visit(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show')
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    barber_service = models.ForeignKey(BarberService, on_delete=models.CASCADE)
    visit_date = models.DateField()
    start_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'), 
        (2, '2 - Fair'), 
        (3, '3 - Good'),
        (4, '4 - Very Good'), 
        (5, '5 - Excellent')
    ]
    
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)



