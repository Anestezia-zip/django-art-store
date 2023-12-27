from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('rate_product/', views.rate_product, name='rate_product_generic'),
    # Первый URL-шаблон с параметром product_id
    path('rate_product/<int:product_id>/', views.rate_product, name='rate_product'),
]
