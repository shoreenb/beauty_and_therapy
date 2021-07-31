from django.shortcuts import render
from .models import Service


def all_services(request):
    """
    A view that shows all services as well as sorting and search queries
    """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)
