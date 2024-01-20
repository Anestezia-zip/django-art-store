from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('edit_painting/<int:painting_id>/',
         views.edit_painting, name='edit_painting'),
    path('delete_painting/<int:painting_id>/',
         views.delete_painting, name='delete_painting'),
]
