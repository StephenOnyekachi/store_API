
from django.db import models

# Create your models here.

class State(models.Model):
    country = models.TextField(max_length=150, blank=True, null=True)
    state = models.TextField(max_length=150)
    def __str__(self):
        return self.state

class LocalGovement(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='local')
    local = models.TextField(max_length=150)
    def __str__(self):
        return self.local
    
class Area(models.Model):
    local = models.ForeignKey(LocalGovement, on_delete=models.CASCADE, related_name='area')
    area = models.TextField(max_length=150)
    def __str__(self):
        return self.area
