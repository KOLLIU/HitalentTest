from django.urls import path

from .views import ChatCreateAPI, ChatDestroyAPI, MessageCreateAPI

urlpatterns = [
    path("", ChatCreateAPI.as_view()),
    path("<int:pk>", ChatDestroyAPI.as_view()),
    path("<int:pk>/messages/", MessageCreateAPI.as_view()),
]