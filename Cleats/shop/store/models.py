from django.db import models
from django.conf import settings

def image_directory_path(instance, filename):
    return 'image_{0}/{1}'.format(instance, filename)

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket_user')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published", null=True)
    items_no = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class BasketItem(models.Model):
    basket =  models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket')
    name = models.TextField(max_length=1500, verbose_name='name')
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True, default=1)



class Item(models.Model):
    name = models.TextField(max_length=1500, verbose_name='name')
    added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True, default=1)
    picture = models.ImageField(upload_to=image_directory_path, blank=True, null=True,)

