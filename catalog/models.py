from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField(default='default.jpg')
    image_2 = models.ImageField(default='default.jpg')
    image_3 = models.ImageField(default='default.jpg')
    discount = models.FloatField(default=0)
    unit = models.CharField(max_length=32)
    price = models.IntegerField()
    sku = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def discount_price(self):
        if self.discount != 0:
            price = self.price - self.price * self.discount / 100
            return round(price, -3) - 100
    