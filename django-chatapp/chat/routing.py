import platform
from django.urls import re_path

from . import consumers

if float(platform.python_version()[0:3]) > 3.6:
    chat_room_consumer = consumers.ChatRoomConsumer.as_asgi()
else:
    cons = consumers.ChatRoomConsumer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]