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
    name = models.CharField(max_length=255)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)
    discount = models.FloatField(default=0)
    unit = models.CharField(max_length=32)
    price = models.IntegerField()
    sku = models.CharField(max_length=255, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

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
        img1 = Image.open(settings.MEDIA_ROOT / "picture_create/free_tar.png")
        img2 = Image.open(settings.MEDIA_ROOT / "sample-out.png")

        img1.paste(img2, (146, 251))

        img1.save(settings.MEDIA_ROOT / f'{self.name}_default.png')

        img = Image.open(settings.MEDIA_ROOT / f'{self.name}_default.png')
        draw = ImageDraw.Draw(img)

        fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/fonts')
        font = ImageFont.truetype(os.path.join(fonts_path, 'PoiretOne-Regular.ttf'), 24)

        text_name = f'{self.name}'
        text_mark = f'{self.sku}'
        text_vol = f'{self.unit}'
        text_name_width = draw.textlength(text_name.upper(), font=font)
        text_mark_width = draw.textlength(text_mark.upper(), font=font)

        draw.text((300 - text_mark_width / 2, 450), text_mark.upper(),(222, 95, 14), font=font)
        draw.text((300 - text_name_width / 2, 490), text_name.upper(),(0, 0, 0), font=font)
        draw.text((160, 560), text_vol, (0, 0, 0), font=font)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=100)
        default_img = File(thumb_io, name=f'{self.name}_default.png')
        
        return default_img

    