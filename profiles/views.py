from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from home.models import PaintingRequest, TemporaryPaintingRequest
from .models import UserProfile
from .forms import PaintingEditForm, TemporaryPaintingEditForm, UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile """
    template = 'profiles/profile.html'
    user_email = request.user.email
    profile = get_object_or_404(UserProfile, user=request.user)
    painting_requests = PaintingRequest.objects.filter(email=user_email)
    temporary_requests = TemporaryPaintingRequest.objects.filter(email=user_email)

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
        'painting_requests': painting_requests,
        'temporary_requests': temporary_requests
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
def edit_painting(request, painting_id, temporary=False):
    """
    - Allows users to edit a painting request, either temporary or permanent, based on the 'temporary' parameter.
    - Handles both GET and POST requests:
        - GET request: Renders the form with the data of the existing painting request.
        - POST request: Validates the submitted form data, saves changes if valid, and redirects to the user's profile.
        If the form is invalid, displays an error message and keeps the user on the editing page.
        - Painting Request - needed for registered users to display in the profile
        - Temporary Painting Request - needed for unregistered users to be able to manage requests during further registration
    """
    if temporary:
        painting = get_object_or_404(TemporaryPaintingRequest, pk=painting_id)
        form_class = TemporaryPaintingEditForm
    else:
        painting = get_object_or_404(PaintingRequest, pk=painting_id)
        form_class = PaintingEditForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Successfully updated painting request')
            return redirect('profile')
        else:
            messages.error(request, f'Failed to update painting request. Please ensure the form is valid')
    else:
        form = form_class(instance=painting)

    context = {
        'form': form,
        'painting': painting,
    }
    return render(request, 'profiles/edit_painting.html', context)


@login_required
def delete_painting(request, painting_id, temporary=False):
    """ Delete a painting request from the store """
    if temporary:
        painting = get_object_or_404(TemporaryPaintingRequest, pk=painting_id)
        painting.delete()
        messages.success(request, 'Temporary painting request deleted!')
    else:
        painting = get_object_or_404(PaintingRequest, pk=painting_id)
        painting.delete()
        messages.success(request, 'Painting request deleted!')

    return redirect('profile')
