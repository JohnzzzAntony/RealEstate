from django.urls import path
from .views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView

urlpatterns = [
    path('', CompanyListView.as_view(), name='company_list'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('create/', CompanyCreateView.as_view(), name='company_create'),
    path('<int:pk>/update/', CompanyUpdateView.as_view(), name='company_update'),
]
