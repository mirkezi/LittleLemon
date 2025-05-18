from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerializer
from .models import Booking, Menu
from rest_framework import generics, viewsets

def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    '''it handles get put and delete calls'''
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer