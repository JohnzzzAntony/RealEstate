from django.contrib import admin
from django.urls import path, include
from dashboards.views import dashboard_view
from rest_framework import routers
from accounts.views_api import UserViewSet
from companies.views_api import InternalTenantCompanyViewSet
from properties.views_api import PropertyViewSet, PropertyUnitViewSet
from leases.views_api import MainLeaseViewSet, SubleaseViewSet
from subtenants.views_api import SubtenantViewSet
from ejari.views_api import EjariRegistrationViewSet
from billing.views_api import BillingViewSet
from documents.views_api import DocumentViewSet
from tasks_notifications.views_api import TaskViewSet
from audit_logs.views_api import AuditLogViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', InternalTenantCompanyViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'units', PropertyUnitViewSet)
router.register(r'main-leases', MainLeaseViewSet)
router.register(r'subleases', SubleaseViewSet)
router.register(r'subtenants', SubtenantViewSet)
router.register(r'ejari', EjariRegistrationViewSet)
router.register(r'billing', BillingViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('companies/', include('companies.urls')),
    path('properties/', include('properties.urls')),
    path('leases/', include('leases.urls')),
    path('subtenants/', include('subtenants.urls')),
    path('billing/', include('billing.urls')),
    path('documents/', include('documents.urls')),
    path('tasks/', include('tasks_notifications.urls')),
    path('reports/', include('reports.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
