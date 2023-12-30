from django.urls import path
from . import views
from functools import partial


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    
    path('edit/<int:painting_id>/', views.edit_painting, name='edit'),
    path('delete/<int:painting_id>/', views.delete_painting, name='delete'),

    path('edit_painting/<int:painting_id>/', partial(views.edit_painting, temporary=True), name='edit_painting'),
    path('delete_painting/<int:painting_id>/', partial(views.delete_painting, temporary=True), name='delete_painting'),
]