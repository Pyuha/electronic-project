from django.db import models

# class AddStuff(models.Model):

#     # image = models.ImageField('image', height_field=100, width_field=100)
#     title = models.CharField('title', max_length=100)
#     price = models.CharField('price', max_length=100)

#     def __str__(self):
#         return f"{self.title} ({self.type})"
    
class ViewStuff (models.Model):

    promo = models.CharField('promo', max_length=1000)
    title = models.CharField('title', max_length=100)
    price = models.CharField('price', max_length=100)

    def __str__(self):
        return f"{self.title} ({self.price})"

