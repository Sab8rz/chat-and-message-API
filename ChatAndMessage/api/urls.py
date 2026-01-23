from django.urls import path
from . import views


urlpatterns = [
    path('chats/', views.create_chat, name='create-chat'),
    path('chats/<int:chat_id>/messages/', views.send_message, name='send-message'),
    path('chats/<int:chat_id>/', views.get_and_delete_chat, name='get-chat'),
    path('chats/<int:chat_id>/', views.get_and_delete_chat, name='delete-chat'),
]

app_name = 'api'