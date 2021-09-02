from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Employee
from datetime import date
from datetime import datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

def index(request):
    user = request.user
    Customer = apps.get_model('customers.Customer')
    pickup_customers = Customer.objects.all()
    try:
        logged_in_employee = Employee.objects.get(user=user)
    except Employee.DoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))
    context = {
            "pickup_customers": pickup_customers,
            "logged_in_employee":logged_in_employee
        }
    return render(request, 'employees/index.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=name, user=user, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

def confirm(request, user_id):
    Customers = apps.get_model('customers.Customer')
    charge_customer = Customers.objects.get(pk = user_id)
    context = { 'charge_customer': charge_customer}
    if request.method == 'POST':
        charge_customer.balance += 10
        charge_customer.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/confirm.html', context)

def select_day(request):
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customers = apps.get_model('customers.Customer')
    pickup_customers = Customers.objects.all()
    current_day = str(date.today())
    weekday = request.POST.get('day_of_the_week')
    pickups = []

    for customer in pickup_customers: 
        customer_start_suspension = str(customer.start_suspension)
        customer_end_suspension = str(customer.end_suspension)
        if  current_day < customer_start_suspension or current_day > customer_end_suspension:     
            if customer.zip_code == logged_in_employee.zip_code and (customer.weekly_pickup_date == weekday or customer.extra_pickup_date == weekday) :
                pickups.append(customer)

    context = { 'pickups': pickups,
                'pickup_customers': pickup_customers,
                'weekday': weekday
    }
    #if request.method == 'POST':
        #return('employees:confirm')
    return render(request, 'employees/daily_view.html', context)
