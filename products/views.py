from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductRating, Wishlist
from django.http import JsonResponse


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'date':  
                sortkey = 'date_created'
            elif sortkey == 'category':
                sortkey = 'category__name'
            elif 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    rating = product.average_rating()
    context = {
        'product': product,
        'rating': rating,
    }
    return render(request, 'products/product_detail.html', context)


def rate_product(request, product_id=None):
    print('Something')
    if request.method == 'POST' and request.user.is_authenticated:
        value = request.POST.get('value')
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        rating, created = ProductRating.objects.get_or_create(product=product, user=user)
        rating.score = value
        rating.save()
        return JsonResponse({'success': True, 'score': value}, safe=False)
    print('Something here')
    return JsonResponse({'success': False})


def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if not created:
        wishlist.delete()
        return JsonResponse({'added': False})
    return JsonResponse({'added': True})