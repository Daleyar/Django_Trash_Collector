from django.urls import path
from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='create'),
    path('pickup/', views.edit, name='edit'),
    path('detail/', views.detail, name='detail'),
    path('suspend/', views.suspend, name='suspend'),
    path('balance/', views.balance, name='balance')
]

