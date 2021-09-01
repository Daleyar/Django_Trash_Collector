from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        email = request.POST.get('email')
        city = request.POST.get('city')
        street_address = request.POST.get('street_address')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=name, user=user, email=email, street_address=street_address, 
        city=city, state=state, zip_code=zip_code
        )
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')