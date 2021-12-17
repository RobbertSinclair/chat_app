import os

import django
from channels.routing import ProtocolTypeRouter
from channels.http import AsgiHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_app.settings")
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
})