from django.db import models

class AddStuff(models.Model):

    promo = models.CharField('promo', max_length=1000)
    title = models.CharField('title', max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.price})"
    
class ViewStuff (models.Model):

    promo = models.CharField('promo', max_length=1000)
    title = models.CharField('title', max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.price})"

