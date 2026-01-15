from rest_framework import serializers

from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"

    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        limit = self.context.get('limit', 20)
        messages = obj.messages.all().order_by('-created_at')[:limit]
        return MessageSerializer(messages, many=True).data


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["chat", "text", "created_at"]
        read_only_fields = ["created_at"]
