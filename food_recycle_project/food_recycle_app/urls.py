from django.urls import path
from . import views

urlpatterns = [
    path('submit_food_donation/', views.submit_food_donation, name='submit_food_donation'),
    path('submit_food_request/', views.submit_food_request, name='submit_food_request'),
    path('donate_list/', views.donate_list, name='donate_list'),
    path('edit_donation/<int:donation_id>/', views.edit_food_donation, name='edit_food_donation')
    # Define URLs for thank you pages or other views as needed.
]