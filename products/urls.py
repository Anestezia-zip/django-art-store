from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('rate_product/<int:product_id>/', views.rate_product, name='rate_product'),
    path('toggle-wishlist/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
]
