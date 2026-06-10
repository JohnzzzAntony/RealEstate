from django.urls import path
from .views import SubtenantListView, SubtenantCreateView

urlpatterns = [
    path('', SubtenantListView.as_view(), name='subtenant_list'),
    path('create/', SubtenantCreateView.as_view(), name='subtenant_create'),
]
