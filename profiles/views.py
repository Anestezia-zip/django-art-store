from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from home.models import PaintingRequest
from .models import UserProfile
from .forms import PaintingEditForm, UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile """
    template = 'profiles/profile.html'
    user_email = request.user.email
    profile = get_object_or_404(UserProfile, user=request.user)
    painting_requests = PaintingRequest.objects.filter(email=user_email)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'user_email': user_email,
        'painting_requests': painting_requests
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def edit_painting(request, painting_id):
    painting = get_object_or_404(PaintingRequest, id=painting_id)
    if request.method == 'POST':
        form = PaintingEditForm(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated painting request')
            return redirect('profile')
        else:
            messages.error(request, 'Failed to update request. Please ensure the form is valid')
    else:
        form = PaintingEditForm(instance=painting)

    context = {
        'form': form,
        'painting': painting,
    }
    return render(request, 'profiles/edit_painting.html', context)


def delete_painting(request, painting_id):
    """ Delete a request from the store """
    painting = get_object_or_404(PaintingRequest, pk=painting_id)
    painting.delete()
    messages.success(request, 'Painting request deleted!')
    return redirect(reverse('profile'))
