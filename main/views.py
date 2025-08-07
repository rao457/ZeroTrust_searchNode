from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.views.generic import TemplateView
# Create your views here.

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class HomeView(TemplateView):
    template_name = 'home.html'