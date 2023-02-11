from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'), 
    path('view_service/',views.view_service, name='view_service'),
    path('search_services/', views.search_services, name='search_services'),
    path('services/<slug:slug>/', views.view_service_category, name='view_service_category'),
]