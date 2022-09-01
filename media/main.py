from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 



img1 = Image.open("./picture_create/free_tar.png")
img2 = Image.open("./sample-out.png")


img1.paste(img2, (
  146,
  251
))

img1.save('new.png')


img = Image.open("new.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('./picture_create/PoiretOne-Regular.ttf', 22)
font2 = ImageFont.truetype('./picture_create/PoiretOne-Regular.ttf', 40)

text_name = "engine-oil-someText"
text_mark = "46"
text_vol = "20L"
text_name_width = draw.textlength(text_name.upper(), font=font)
text_mark_width = draw.textlength(text_mark.upper(), font=font)

draw.text((300 - text_name_width / 2, 510), text_name.upper(),(0, 0, 0), font=font)
draw.text((290 - text_mark_width / 2, 450), text_mark.upper(),(222, 95, 14), font=font2)
draw.text((160, 560), text_vol, (0, 0, 0), font=font)

img.save('new.png')