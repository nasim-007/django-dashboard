from django.db import models

# Create your models here.
class helloWorld(models.Model):
    simple_text = models.CharField(max_length=200)

    def __str__(self):
        return self.simple_text

