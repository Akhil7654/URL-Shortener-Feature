from django.db import models

class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.original_url