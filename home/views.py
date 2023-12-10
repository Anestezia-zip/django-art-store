from django.shortcuts import redirect, render
from .forms import PaintingRequestForm
from .models import PaintingRequest

def index(request):
    form = PaintingRequestForm()
    return render(request, 'home/index.html', {'form': form})

def create_painting_request(request):
    if request.method == 'POST':
        form = PaintingRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaintingRequestForm()
    
    return render(request, 'home/index.html', {'form': form})


def gallery(request):
    return render(request, 'home/gallery.html')