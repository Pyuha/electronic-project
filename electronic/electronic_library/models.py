from django.db import models

class AddStuff(models.Model):

    title = models.CharField('title', max_length=100)
    type = models.CharField('type', max_length=100)

    def __str__(self):
        return f"{self.title} ({self.type})"