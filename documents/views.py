from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Document

class DocumentListView(ListView):
    model = Document
    template_name = 'documents/document_list.html'
    context_object_name = 'documents'
