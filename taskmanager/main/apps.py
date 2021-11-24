from django.apps import AppConfig
from django.db.models import signals


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from . import signals
    
