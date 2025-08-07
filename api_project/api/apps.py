from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        # This forces Django to recognize models
        from . import models
        models.Author  # Reference the models
        models.Book