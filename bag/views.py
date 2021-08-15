from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return show the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product/service to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    option = None
    if 'product_option' in request.POST:
        option = request.POST['product_option']
    bag = request.session.get('bag', {})

    if option:
        if item_id in list(bag.keys()):
            if option in bag[item_id]['items_by_option'].keys():
                bag[item_id]['items_by_option'][option] += quantity
                messages.success(
                    request, f'Updated {option.upper()} {product.name} quantity to {bag[item_id]["items_by_option"][option]}')
            else:
                bag[item_id]['items_by_option'][option] = quantity
                messages.success(
                    request, f'Option {option.upper()} {product.name} has been added to your bag')
        else:
            bag[item_id] = {'items_by_option': {option: quantity}}
            messages.success(
                request, f'Option {option.upper()} {product.name} has been added to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'{product.name} quantity has been updated to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'{product.name} has been added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the chosen product to the required amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    option = None
    if 'product_option' in request.POST:
        option = request.POST['product_option']
    bag = request.session.get('bag', {})

    if option:
        if quantity > 0:
            bag[item_id]['items_by_option'][option] = quantity
            messages.success(
                request, f'Updated {product.name}{option.upper()} quantity to {bag[item_id]["items_by_option"][option]}')
        else:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_option']:
                bag.pop(item_id)
                messages.success(
                    request, f'Option {option.upper()} {product.name} has been removed from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'{product.name} quantity has been updated to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'{product.name} has been removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        option = None
        if 'product_option' in request.POST:
            option = request.POST['product_option']
        bag = request.session.get('bag', {})

        if option:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_option']:
                bag.pop(item_id)
                messages.success(
                    request, f'Option {option.upper()} {product.name} has been removed from your bag')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'{product.name} has been removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
