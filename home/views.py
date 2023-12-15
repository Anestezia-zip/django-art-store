from django.shortcuts import redirect, render
from .forms import PaintingRequestForm
from .models import PaintingRequest
from django.contrib import messages


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
    initial_email = request.user.email if request.user.is_authenticated else ''

    if request.method == 'POST':
        form = PaintingRequestForm(request.POST, request.FILES)
        if form.is_valid():
            painting_request = form.save(commit=False)
            painting_request.email = initial_email
            painting_request.save()
            messages.success(request, 'Successfully sent request!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to send a request. Please ensure the form is valid.')
    else:
        form = PaintingRequestForm(initial={'email': initial_email})

    painting_requests = PaintingRequest.objects.all()
    context = {
        'form': form,
        'painting_requests': painting_requests
    }

    return render(request, 'home/index.html', context)


def gallery(request):
    return render(request, 'home/gallery.html')