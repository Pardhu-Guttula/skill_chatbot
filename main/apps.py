from django.apps import AppConfig
from sentence_transformers import SentenceTransformer


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'

    def ready(self):
        # Load the SentenceTransformer model during app startup
        from . import demo  # Import your demo module
        demo.load_model()