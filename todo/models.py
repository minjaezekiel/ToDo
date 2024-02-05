from django.db import models

# LightOne Minja
class Todo(models.Model):
    task = models.CharField(max_length = 255)
    completed = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title
