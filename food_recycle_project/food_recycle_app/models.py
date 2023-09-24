from django.db import models

# Create your models here.

class RestaurantDonation(models.Model):
    restaurant_name = models.CharField(max_length=100)
    food_description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    fulfilled = models.BooleanField(default=False)

class NGORequest(models.Model):
    ngo_name = models.CharField(max_length=100)
    food_request = models.TextField()
    quantity_requested = models.DecimalField(max_digits=10, decimal_places=2)
    fulfilled = models.BooleanField(default=False)