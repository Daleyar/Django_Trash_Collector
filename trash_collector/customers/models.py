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
    current_balance = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    weekly_pickup_date = models.CharField(max_length=50)
    extra_pickup_date = models.CharField(max_length=50)
    account_suspension = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    