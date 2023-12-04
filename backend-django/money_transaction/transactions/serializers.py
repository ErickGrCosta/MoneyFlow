from rest_framework import serializers
from .models import Transaction
from users.serializers import CustomUserSerializer

class TransactionSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer(read_only=True)
    receiver = CustomUserSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'timestamp', 'transaction_status']
