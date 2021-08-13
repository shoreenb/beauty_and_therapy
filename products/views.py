from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Option


def all_products(request):
    """
    A view that shows all products as well as sorting and search
    queries for products and services
    """

    products = Product.objects.all()
    categories = None
    query = None
    sort = None
    direction = None
    heading = 'Products & Services'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            if len(categories) == 1:
                heading = categories[0].friendly_name
            else:
                for category in categories:
                    if 'products' in category.name:
                        heading = 'Products & Services'
                        break
                    else:
                        if 'services' in category.name:
                            heading = 'Services'

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('home'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'heading': heading,
    }

    return render(
        request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view that shows the details of an individual product
    """

    product = get_object_or_404(Product, pk=product_id)
    options = None

    if 'option' in request.GET:
        options = request.GET['option']
        options = list(Option.objects.filter(name__in=options))

    context = {
        'product': product,
        'options': options,
    }

    return render(request, 'products/product_detail.html', context)
