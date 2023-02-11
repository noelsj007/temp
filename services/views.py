from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from services.models import Services, ServiceProvider

# Create your views here.

def services(request):
    popular_services = Services.objects.filter(status=Services.ACTIVE)[0:4]
    popular_service_providers = ServiceProvider.objects.all().order_by('star').values()[0:4]
    services = Services.objects.all()
    
    return render(request, 'services.html', {
    'popular_service_providers': popular_service_providers,
    'popular_services': popular_services,
    'services': services,
    })

def view_service(request):
    services = Services.objects.all()
    serpro = ServiceProvider.objects.all()
    return render(request, 'view_service.html', {
    'services': services,
    'serpro': serpro,
    }
    )

def search_services(request):
    service_query = request.GET.get('service_query', '')
    services = None
    if service_query:
        services = Services.objects.filter(status=Services.ACTIVE).filter(Q(title__icontains=service_query) | Q(description__icontains=service_query))
        #results2 = ServiceProvider.objects.all() 

    return render(request, 'search_services.html', {
    'service_query': service_query,
    'services': services,
    })   



def view_service_category(request, slug):
    service = get_object_or_404(Services, slug=slug)
    return render(request, 'view_service_category.html', { 
    'service': service,
    })













