from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/conversation/(?P<conversation_id>\d+)/$', consumers.ConversationConsumer.as_asgi(), name='websocket'),
]