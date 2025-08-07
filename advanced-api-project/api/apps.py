from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'
    verbose_name = 'API Application'
    
    def ready(self):
        # This forces model registration
        from . import models
        models.Author
        models.Book