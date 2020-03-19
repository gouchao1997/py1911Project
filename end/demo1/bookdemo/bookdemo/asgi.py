"""
ASGI config for bookdemo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
#指明django的配置文件为 bookdemo.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookdemo.settings')

application = get_asgi_application()
#django自带的web服务器
