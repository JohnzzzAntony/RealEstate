from django.urls import path
from .views import BillingListView, BillingCreateView

urlpatterns = [
    path('', BillingListView.as_view(), name='billing_list'),
    path('create/', BillingCreateView.as_view(), name='billing_create'),
]
