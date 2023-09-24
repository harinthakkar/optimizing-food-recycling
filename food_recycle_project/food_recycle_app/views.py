from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from django.shortcuts import render, redirect
from .models import RestaurantDonation, NGORequest

def submit_food_donation(request):
    if request.method == 'POST':
        restaurant_name = request.POST.get('restaurant_name')
        food_description = request.POST.get('food_description')
        quantity = request.POST.get('quantity')
        fulfilled_donation = 'fulfilled_donation' in request.POST

        # Save the donation to the database (RestaurantDonation model)
        RestaurantDonation.objects.create(
            restaurant_name=restaurant_name,
            food_description=food_description,
            quantity=quantity,
            fulfilled=fulfilled_donation
        )
        

    return render(request, 'donate.html')

def submit_food_request(request):
    if request.method == 'POST':
        ngo_name = request.POST.get('ngo_name')
        food_request = request.POST.get('food_request')
        quantity_requested = request.POST.get('quantity_requested')
        fulfilled_request = 'fulfilled_request' in request.POST

        # Save the request to the database (NGORequest model)
        NGORequest.objects.create(
            ngo_name=ngo_name,
            food_request=food_request,
            quantity_requested=quantity_requested,
            fulfilled=fulfilled_request
        )
        

    return render(request, 'order.html')


    # def homepage
def donate_list(request):
    food_items = RestaurantDonation.objects.all()
    return render(request, 'donate_list.html', {'food_items': food_items})

def edit_food_donation(request, donation_id):
    donation = get_object_or_404(RestaurantDonation, id=donation_id)

    if request.method == 'POST':
        restaurant_name = request.POST.get('restaurant_name')
        food_description = request.POST.get('food_description')
        quantity = request.POST.get('quantity')
        fulfilled_donation = 'fulfilled_donation' in request.POST

        donation.restaurant_name = restaurant_name
        donation.food_description = food_description
        donation.quantity = quantity
        donation.fulfilled = fulfilled_donation
        donation.save()

        return redirect('donate_list')

    return render(request, 'update.html', {'donation': donation})