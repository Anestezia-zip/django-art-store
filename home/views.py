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
                # Если пользователь залогинен, сохраняем запрос с привязкой к пользователю
                painting_request = form.save(commit=False)
                painting_request.user = request.user
                painting_request.save()
            else:
                # Если пользователь не залогинен, сохраняем запрос временно
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
            message = f'New request received:\n\nDescription: {form.cleaned_data.get("description")}\nSize: {form.cleaned_data.get("size")}\nEmail: {form.cleaned_data.get("email")}'
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['receiver@example.com', ]  # email получателя
            send_mail(subject, message, email_from, recipient_list)

            messages.success(request, 'Successfully sent request!')
            if request.user.is_authenticated:
                return redirect('profile')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Failed to send a request. Please ensure the form is valid.')
    else:
        form = PaintingRequestForm()

    painting_requests = PaintingRequest.objects.all()
    context = {
        'form': form,
        'painting_requests': painting_requests
    }

    return render(request, 'home/index.html', context)


def gallery(request):
    return render(request, 'home/gallery.html')