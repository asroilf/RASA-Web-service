from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.HyperlinkedModelSerialzer):

    class Meta:
        model = Message
        field = ["idd", "message", "response"]

