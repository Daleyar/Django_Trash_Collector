from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5) 
    current_balance = models.FloatField(default=0)
    weekly_pickup_date = models.DateField(null=True, blank=True)
    extra_pickup_date = models.DateField(null=True, blank=True)
    start_suspension = models.DateField(null=True, blank=True) 
    end_suspension = models.DateField(null=True, blank=True) 
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    