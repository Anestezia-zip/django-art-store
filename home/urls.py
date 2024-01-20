from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/',
         views.create_painting_request, name='create_painting_request'),
]
