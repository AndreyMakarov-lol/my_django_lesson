from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from orders.models import SalesOrder

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Убедитесь, что username включен


class OrderSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)  # Сериализация связанного пользователя
    class Meta:
        model = SalesOrder
        fields = ['amount', 'description', 'user', 'product']