from django.db import models

# Create your models here.


class Conversation(models.Model):
    user_input = models.TextField()
    model_response = models.TextField()
