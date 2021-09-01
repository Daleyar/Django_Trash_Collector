from django.core.checks import messages
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Customer
# Create your views here.
#from django.urls import reverse_lazy, reverse
#from django.views import generic

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        pass

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        email = request.POST.get('email')
        city = request.POST.get('city')
        street_address = request.POST.get('street_address')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_date = request.POST.get('weekly_pickup_date')
        extra_pickup_date = request.POST.get('extra_pickup_date')
        new_cust = Customer(name=name, user=user, email=email, street_address=street_address,
        city=city, state=state, zip_code=zip_code, weekly_pickup_date=weekly_pickup_date,
        extra_pickup_date=extra_pickup_date
        )
        new_cust.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')

def edit(request):
    user = request.user
    logged_in_customer = Customer.objects.get(user=user)
    if request.method == "POST":
        logged_in_customer.name = request.POST.get('name')
        logged_in_customer.email = request.POST.get('email')
        logged_in_customer.street_address = request.POST.get('street_address')
        logged_in_customer.city = request.POST.get('city')
        logged_in_customer.state = request.POST.get('state')
        logged_in_customer.zip_code = request.POST.get('zip_code')
        logged_in_customer.weekly_pickup_date = request.POST.get('weekly_pickup_date')
        logged_in_customer.extra_pickup_date = request.POST.get('extra_pickup_date')
        logged_in_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'logged_in_customer': logged_in_customer
    }
    return render(request, 'customers/pickup.html', context)

def detail(request):
    user = request.user
    logged_in_customer = Customer.objects.get(user=user)
    context = {
        'logged_in_customer':logged_in_customer
    }
    return render(request, 'customers/detail.html', context)


def balance(request):
    user = request.user
    logged_in_customer = Customer.objects.get(user=user)
    return render(request, 'customers/balance.html')


def suspend(request):
    user = request.user
    logged_in_customer = Customer.objects.get(user=user)

    if request.method == "POST":
        logged_in_customer.start_suspension = request.POST.get("start_suspension")
        logged_in_customer.end_suspension = request.POST.get("end_suspension")
        logged_in_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/suspend.html')
