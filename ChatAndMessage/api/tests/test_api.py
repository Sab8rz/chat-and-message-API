import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api import models


@pytest.mark.django_db
def test_create_chat():
    response = APIClient().post(reverse('api:create-chat'), {'title': 'Тестовый чат'})
    assert response.status_code == status.HTTP_201_CREATED
    assert models.Chat.objects.count() == 1


@pytest.mark.django_db
def test_send_message():
    chat = models.Chat.objects.create(title='Тестовый чат')
    url = reverse('api:send-message', args=[chat.id])
    response = APIClient().post(url, {'text': 'всем привет'})
    assert response.status_code == status.HTTP_201_CREATED
    assert models.Message.objects.count() == 1


@pytest.mark.django_db
def test_get_chat_and_messages():
    chat = models.Chat.objects.create(title='Тестовый чат')
    models.Message.objects.create(chat=chat, text='привет')
    url = reverse('api:get-chat', args=[chat.id])
    response = APIClient().get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['messages']) == 1


@pytest.mark.django_db
def test_delete_chat():
    chat = models.Chat.objects.create(title='Беседа №1')
    url = reverse('api:delete-chat', args=[chat.id])
    response = APIClient().delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert models.Chat.objects.count() == 0