from django.db import models

class Quote(models.Model):
    text = models.TextField()
    quote_author = models.TextField()