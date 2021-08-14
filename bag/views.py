from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view to return show the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product/service to the shopping bag """

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
            else:
                bag[item_id]['items_by_option'][option] = quantity
        else:
            bag[item_id] = {'items_by_option': {option: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the chosen product to the required amount """

    quantity = int(request.POST.get('quantity'))
    option = None
    if 'product_option' in request.POST:
        option = request.POST['product_option']
    bag = request.session.get('bag', {})

    if option:
        if quantity > 0:
            bag[item_id]['items_by_option'][option] = quantity
        else:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        option = None
        if 'product_option' in request.POST:
            option = request.POST['product_option']
        bag = request.session.get('bag', {})

        if option:
            del bag[item_id]['items_by_option'][option]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
