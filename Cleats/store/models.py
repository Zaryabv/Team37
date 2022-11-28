from django.db import models
from django.conf import settings
def image_directory_path(instance, filename):
    return 'image_{0}/{1}'.format(instance, filename)
import uuid

class ImageFiles(models.Model):
    file = models.FileField(upload_to=image_directory_path)

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket_user')
    date_made = models.DateTimeField(auto_now_add=True, verbose_name="date made", null=True)
    items_no = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class BasketItem(models.Model):
    basket =  models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket')
    name = models.TextField(max_length=1500, verbose_name='basket_name')
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True, default=1)
    picture = models.ImageField(upload_to=image_directory_path, blank=True, null=True,)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Item(models.Model):
    name = models.TextField(max_length=1500, verbose_name='name')
    added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True, default=1)
    picture = models.ImageField(upload_to=image_directory_path, blank=True, null=True,)
    description = models.TextField(max_length=1500, null=True, blank=True)

class HistoryItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_history')
    name = models.TextField(max_length=1500, verbose_name='history_name')
    added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True, default=1)
    picture = models.ManyToManyField(ImageFiles, related_name='history_image')
