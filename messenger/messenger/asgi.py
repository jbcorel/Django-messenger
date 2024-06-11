import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import chats.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messenger.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(), 
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chats.routing.websocket_urlpatterns
            )
        )
    )
})

