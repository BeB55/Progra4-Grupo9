from django.urls import path, include
from . import views

app_name = 'telegram_chat'

urlpatterns = [
    path('telegram_chat/', views.chat_view, name='chat_view'),
    path("chat/api/post/", views.post_message, name="post_message"),
]