import os
from io import BytesIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from django.conf import settings
from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True, default='default.png')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='brand/', blank=True, null=True, default='default.png')

    def __str__(self):
        return self.name


class AbstractProduct(models.Model):
    title = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product/', blank=True, null=True, default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def discount_price(self):
        if self.discount > 0:
            price = self.price - self.price * self.discount / 100
            return round(price, -3) - 100


class ProductLubricant(AbstractProduct):
    VOLUME_CHOICES = [
        ('barrel', 'barrel'),
        ('canister', 'canister'),
        ('other', 'other'),
    ]

    volume = models.CharField(max_length=255, blank=True, null=True, choices=VOLUME_CHOICES)
    unit = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)

    def get_unit(self):
        if not self.unit:
            if self.volume == 'barrel':
                return '400 L'
            elif self.volume == 'canister':
                return '20 L'
        return self.unit

    def get_thumbnail(self):
        if self.thumbnail:
            return f'{self.thumbnail.url}'
        else:
            self.thumbnail = self.make_thumbnail()
            self.save()
            return f'{self.thumbnail.url}'

    def make_thumbnail(self):

        img = Image.open(f"{settings.MEDIA_ROOT}/picture_create/free_tar.png")
        draw = ImageDraw.Draw(img)

        fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/fonts')
        font_mark = ImageFont.truetype(os.path.join(fonts_path, 'Manrope-Bold.ttf'), 28)
        font_name = ImageFont.truetype(os.path.join(fonts_path, 'Manrope-Bold.ttf'), 16)
        font = ImageFont.truetype(os.path.join(fonts_path, 'Manrope-Bold.ttf'), 18)

        text_name = f'{self.title}'
        text_brand = f'{self.brand.name}'
        text_vol = f'{self.get_unit()}'
        text_name_width = draw.textlength(text_name.upper(), font=font_name)
        text_brand_width = draw.textlength(text_brand.upper(), font=font_mark)

        draw.text((395 - text_brand_width / 2, 315), text_brand.upper(), (222, 95, 14), font=font_mark)
        draw.text((395 - text_name_width / 2, 350), text_name.upper(), (32, 32, 32), font=font_name)
        draw.text((300, 380), text_vol, (80, 80, 80), font=font)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=100)
        default_img = File(thumb_io, name=f'{self.title}_default.png')

        return default_img

    def __str__(self):
        return self.title
