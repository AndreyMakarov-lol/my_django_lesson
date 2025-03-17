from django.shortcuts import render
from orders.serializers import OrderSerializer
from orders.models import SalesOrder
from rest_framework.viewsets import ModelViewSet


# Create your views here.
def order_page(request):
    return render(request, 'index.html', {'orders':SalesOrder.objects.all()})

class OrderViews(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer

def orders_app(request):
    return render(request, 'main.html')