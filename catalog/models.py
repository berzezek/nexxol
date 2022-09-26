from django.db import models
from django.conf import settings
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from io import BytesIO
from django.core.files import File
import os


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    isActive = models.BooleanField(default=True)


class Product(models.Model):
    TAR_CHOICES = [
        ('barrel', 'barrel'),
        ('kanister', 'kanister'),
        ('other', 'other'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)
    tara = models.CharField(max_length=16, choices=TAR_CHOICES, default="other")
    discount = models.FloatField(default=0)
    unit = models.CharField(max_length=32, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    product_mark = models.CharField(max_length=32, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_unit(self):
        if not self.unit:
            if self.tara == 'barrel':
                return '400 L'
            elif self.tara == 'kanister':
                return '20 L'
        return self.unit

    def discount_price(self):
        if self.discount > 0:
            price = self.price - self.price * self.discount / 100
            return round(price, -3) - 100

    def get_image_1(self):
        if self.image_1:
            return f'{self.image_1.url}' 
        return null

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

        text_name = f'{self.name}'
        text_mark = f'{self.product_mark}'
        text_vol = f'{self.get_unit()}'
        text_name_width = draw.textlength(text_name.upper(), font=font_name)
        text_mark_width = draw.textlength(text_mark.upper(), font=font_mark)

        draw.text((395 - text_mark_width / 2, 315), text_mark.upper(),(222, 95, 14), font=font_mark)
        draw.text((395 - text_name_width / 2, 350), text_name.upper(),(32, 32, 32), font=font_name)
        draw.text((300, 380), text_vol, (80, 80, 80), font=font)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=100)
        default_img = File(thumb_io, name=f'{self.name}_default.png')
        
        return default_img

    