from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Option
from .forms import ProductForm


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


@login_required
def add_product(request):
    """ Add a product/service to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Invalid Request: Only admin can add products/services.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product/service!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product/service. \
            Please check that the details in the form are valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'on_add_product_page': True
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product/service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Invalid Request: Only admin can edit products/services.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successful!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Update Failed. \
            Please check that the details in the form are valid ')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'on_edit_product_page': True
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product/service from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Invalid Request: Only admin can delete products/services.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product/Service deleted!')
    return redirect(reverse('products'))
