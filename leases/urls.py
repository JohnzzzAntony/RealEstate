from django.urls import path
from .views import MainLeaseListView, MainLeaseDetailView, MainLeaseCreateView, SubleaseListView, SubleaseCreateView

urlpatterns = [
    path('main/', MainLeaseListView.as_view(), name='main_lease_list'),
    path('main/<int:pk>/', MainLeaseDetailView.as_view(), name='main_lease_detail'),
    path('main/create/', MainLeaseCreateView.as_view(), name='main_lease_create'),
    path('sub/', SubleaseListView.as_view(), name='sublease_list'),
    path('sub/create/', SubleaseCreateView.as_view(), name='sublease_create'),
]
