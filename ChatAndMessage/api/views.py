from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models


@api_view(['POST'])
def create_chat(request):
    title = request.data['title'].strip()
    if not title:
        return Response({'error': 'Введите название чата'}, status=status.HTTP_400_BAD_REQUEST)
    if len(title) > 200:
        return Response({'error': 'Максимальная длина 200 символов'}, status=status.HTTP_400_BAD_REQUEST)
    chat = models.Chat.objects.create(title=title)
    serializer = serializers.ChatSerializer(chat)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def send_message(request, chat_id):
    text = request.data['text'].strip()
    if not text:
        return Response({'error': 'Сообщение не может быть пустым'}, status=status.HTTP_400_BAD_REQUEST)
    if len(text) > 5000:
        return Response({'error': 'Максимальная длина 5000 символов'}, status=status.HTTP_400_BAD_REQUEST)
    chat = get_object_or_404(models.Chat, id=chat_id)
    message = models.Message.objects.create(chat=chat, text=text)
    serializer = serializers.MessageSerializer(message)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def get_and_delete_chat(request, chat_id):
    if request.method == 'GET':
        limit = request.GET.get('limit', 20)
        try:
            limit = int(limit)
        except ValueError:
            limit = 20
        if limit > 100:
            limit = 100
        chat = get_object_or_404(models.Chat, id=chat_id)
        messages = models.Message.objects.filter(chat=chat).order_by('-created_at')[:limit]
        return Response({
            'chat': serializers.ChatSerializer(chat).data,
            'messages': serializers.MessageSerializer(messages, many=True).data
        }, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        chat = get_object_or_404(models.Chat, id=chat_id)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)