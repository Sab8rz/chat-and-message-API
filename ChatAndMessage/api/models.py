from django.db import models
from django.utils.text import Truncator


class Chat(models.Model):
    title = models.CharField(verbose_name='Название чата')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания чата')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return f"ID: {self.id}, Название чата: {self.title}"



class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='message', verbose_name='id чата')
    text = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время написания сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        truncated_text = Truncator(self.text).chars(30, truncate='...')
        return f"Сообщение в чате '{self.chat.title}': {truncated_text}"