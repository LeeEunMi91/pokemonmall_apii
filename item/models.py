from django.db import models
import random
from user.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

def get_item_image_path(instance, filename):
    filename = str(random.randint(10000, 100000)) + filename
    path = 'item_images/%s' % (filename)
    return path


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to=get_item_image_path)


class UserItem(models.Model):
    user = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)