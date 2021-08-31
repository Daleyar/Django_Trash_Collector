from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Customer
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CustomerForm

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
        new_cust = Customer(name=name, user=user)
        new_cust.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')



#def pickup(request):
    #user = request.user
    #logged_in_customer = Customer.objects.get(user=user)

class ProfileView(generic.CreateView):
    form_class = CustomerForm
    success_url = reverse_lazy('home')
    template_name = 'customers/create.html'

class ProfileDetail(generic.DetailView):
    template_name = 'customers/detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Customer,id=id_)
