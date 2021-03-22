from django.db import models

# Create your models here.
"""
creating class editor and assigning models
"""
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()