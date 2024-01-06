from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductRating, Wishlist
from django.http import JsonResponse


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().order_by('pk')
    wishlist_items = []
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
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
        'wishlist_item_ids': wishlist_items
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user = request.user
        rating = ProductRating.objects.filter(product=product, user=user).first()
    else:
        rating = None

    ratingAverage = product.average_rating()
    context = {
        'product': product,
        'rating': rating,
        'ratingAverage': ratingAverage,
    }
    return render(request, 'products/product_detail.html', context)


def rate_product(request, product_id=None):
    if request.method == 'POST' and request.user.is_authenticated:
        value = request.POST.get('value')
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        rating, created = ProductRating.objects.get_or_create(product=product, user=user)
        rating.score = value
        rating.checked = True
        rating.save()
        return JsonResponse({'success': True, 'score': rating.score})
    return JsonResponse({'success': False})


def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()
    
    if wishlist_item:
        wishlist_item.delete()
        return JsonResponse({'added': False})
    else:
        Wishlist.objects.create(user=request.user, product=product)
        return JsonResponse({'added': True})


def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()

    if wishlist_item:
        wishlist_item.delete()
        return JsonResponse({'removed': True})
    else:
        return JsonResponse({'removed': False})


def view_wishlist(request):
    products = Product.objects.all()
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)

    context = {
        'products': products,
        'wishlist_item_ids': wishlist_items
    }
    return render(request, 'products/wishlist.html', context)
