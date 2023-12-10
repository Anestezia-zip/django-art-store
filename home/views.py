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
            form.save()  # Сохраняем данные из формы в базу данных
            return redirect('home')  # Перенаправляем на страницу 'home' после успешного сохранения
    else:
        form = PaintingRequestForm()
    
    return render(request, 'home/index.html', {'form': form})
