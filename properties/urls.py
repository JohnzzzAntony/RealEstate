from django.urls import path
from .views import PropertyListView, PropertyDetailView, PropertyCreateView, PropertyUpdateView, PropertyUnitListView, PropertyUnitDetailView, PropertyUnitCreateView

urlpatterns = [
    path('', PropertyListView.as_view(), name='property_list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('create/', PropertyCreateView.as_view(), name='property_create'),
    path('<int:pk>/update/', PropertyUpdateView.as_view(), name='property_update'),
    path('units/', PropertyUnitListView.as_view(), name='unit_list'),
    path('units/<int:pk>/', PropertyUnitDetailView.as_view(), name='unit_detail'),
    path('units/create/', PropertyUnitCreateView.as_view(), name='unit_create'),
]
