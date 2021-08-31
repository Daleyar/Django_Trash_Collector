from django import forms
from django.forms import ModelForm
from .models import Customer
 
#class CustomerForm(forms.ModelForm):
    #class Meta:
        #model = Customer
        #fields = [
            #'name',
           # 'email',
           # 'street_address',
           # 'city',
          #  'state',
           # 'zip_code'
       # ]

#class SetPickupDate(forms.ModelForm):
   # class Meta:
     #   model = Customer
     #   fields = [
     #       'weekly_pickup_date',
      #      'extra_pickup_date'
     #   ]