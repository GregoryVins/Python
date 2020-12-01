from django.db import models

from authapp.models import UserProfile


class Message(models.Model):
    """Модель сообщения пользователя."""
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='senderuser')
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recipientuser')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message} ({self.sender.nickname})'
