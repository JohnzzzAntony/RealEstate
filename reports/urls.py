from django.urls import path
from .views import report_list, occupancy_report, revenue_report

urlpatterns = [
    path('', report_list, name='report_list'),
    path('occupancy/', occupancy_report, name='occupancy_report'),
    path('revenue/', revenue_report, name='revenue_report'),
]
