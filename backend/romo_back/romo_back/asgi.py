"""
ASGI config for romo_back project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from livestreaming.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "romo_back.settings")

application = ProtocolTypeRouter({
"http": get_asgi_application(),
"websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns,
        )
    ),
})