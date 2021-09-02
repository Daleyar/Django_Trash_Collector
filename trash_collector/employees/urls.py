from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='create'),
    path('daily_view/', views.select_day, name='daily_view'),
    path('confirm/<int:user_id>', views.confirm, name='confirm')
]
