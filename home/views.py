from django.shortcuts import redirect, render
from .forms import PaintingRequestForm
from .models import PaintingRequest
from django.contrib import messages


def index(request):
    form = PaintingRequestForm()
    return render(request, 'home/index.html', {'form': form})


def create_painting_request(request):
    painting_requests = PaintingRequest.objects.all()
    if request.method == 'POST':
        form = PaintingRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully send request!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to send a request. Please ensure the form is valid.')
    else:
        form = PaintingRequestForm()

    context = {
        'form': form,
        'painting_requests': painting_requests
    }
    
    return render(request, 'home/index.html', context)


def gallery(request):
    return render(request, 'home/gallery.html')