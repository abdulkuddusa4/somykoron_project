from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r"ws/waiting_room/", consumer.MyConsumer.as_asgi()),
]