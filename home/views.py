from django.shortcuts import redirect, render
from .forms import PaintingRequestForm
from .models import PaintingRequest, TemporaryPaintingRequest
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    initial_email = request.user.email if request.user.is_authenticated else ''
    form = PaintingRequestForm(initial={'email': initial_email})
    painting_requests = PaintingRequest.objects.all()

    context = {
        'form': form,
        'painting_requests': painting_requests
    }
    return render(request, 'home/index.html', context)


def create_painting_request(request):
    if request.method == 'POST':
        form = PaintingRequestForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                # If the user is logged in, save the request with user binding
                painting_request = form.save(commit=False)
                painting_request.user = request.user
                painting_request.save()
            else:
                # If the user is not logged in, save the request temporarily
                temporary_request = TemporaryPaintingRequest(
                    email=form.cleaned_data.get('email'),
                    description=form.cleaned_data.get('description'),
                    size=form.cleaned_data.get('size'),
                    add_signature=form.cleaned_data.get('add_signature'),
                    examples=form.cleaned_data.get('examples'),
                    examples2=form.cleaned_data.get('examples2')
                )
                temporary_request.save()

            subject = 'New Painting Request'
            message = (
                f'New request received:\n\n'
                f'Description: {form.cleaned_data.get("description")}\n'
                f'Size: {form.cleaned_data.get("size")}\n'
                f'Email: {form.cleaned_data.get("email")}'
            )
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['plekatybtc@gmail.com']
            send_mail(subject, message, email_from, recipient_list)

            messages.success(request, 'Successfully sent request!')
            return redirect('home')
        else:
            messages.error(request,
                           'Failed to send a request. '
                           'Please ensure the form is valid.')
    else:
        form = PaintingRequestForm()

    painting_requests = PaintingRequest.objects.all()
    context = {
        'form': form,
        'painting_requests': painting_requests
    }

    return render(request, 'home/index.html', context)
