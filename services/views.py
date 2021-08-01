from django.shortcuts import render, get_object_or_404
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


def service_detail(request, service_id):
    """
    A view that shows the details of an individual service
    """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)
