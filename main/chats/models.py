from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Chat(models.Model):
    title = models.CharField(blank=False, null=False,
                             validators=[
                                 MinLengthValidator(1, 'Название чата не может быть пустым')
                             ], max_length=200,
                             verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Время отправки")

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"

    def __str__(self):
        return f"{self.title}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE,
                             verbose_name="Чат", related_name="messages")
    text = models.TextField(blank=False, null=False,
                            validators=[
                                MinLengthValidator(1,
                                                   'Сообщение не может быть пустым'),
                                MaxLengthValidator(5000,
                                                   'Длина сообщения не должна превышать 5000 символов')
                            ],
                            verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Время отправки")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"({self.chat.title}) {self.text}"
