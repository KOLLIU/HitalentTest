from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response

from .models import Chat
from .serializers import ChatSerializer, MessageSerializer


class ChatCreateAPI(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDestroyAPI(RetrieveDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_object(self):
        return get_object_or_404(Chat, pk=self.kwargs['pk'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        try:
            limit = int(self.request.query_params.get('limit', 20))
        except (ValueError, TypeError):
            limit = 20
        if limit < 1:
            limit = 20
        elif limit > 100:
            limit = 100
        context['limit'] = limit
        return context


class MessageCreateAPI(CreateAPIView):
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        chat = get_object_or_404(Chat, pk=kwargs['pk'])

        data = request.data.copy()
        data['chat'] = chat.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )