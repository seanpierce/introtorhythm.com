import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont


def resize_image(image, size: int):
    """
    Resizes an image to a square based on the provided size.
    """

    width, height = image.size

    if width < height:
        image = image.resize((size, int(height * (size / width))), Image.ANTIALIAS)
    elif height < width:
        image = image.resize((int(width * (size / height)), size), Image.ANTIALIAS)
    else: 
        image = image.resize((size, size), Image.ANTIALIAS) 

    # reset vars 
    width, height = image.size

    image = image.crop((
        (width - size) // 2,
        (height - size) // 2,
        (width + size) // 2,
        (height + size) // 2
    ))

    return image
    

def crop_to_circle(image):
    """
    Uses a circular mask to create a 'cropped' circle of an image.
    """
    npImage = np.array(image)
    h, w =image.size
    alpha = Image.new('L', (h * 100, w * 100), 0)
    alpha = alpha.resize((h, w), Image.ANTIALIAS)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w],0, 360, fill = 255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage, npAlpha))
    return Image.fromarray(npImage)


def add_title_with_text(image):
    w, _ = image.size
    text = "Intro To Rhythm"
    font = ImageFont.truetype('./assets/RobotoMono.ttf', 60)
    width = font.getlength(text)
    text_start = (w - width) // 2
    image_draw = ImageDraw.Draw(image)
    image_draw.text((text_start, 50), text, '#fff', font=font)
    return image


def add_url_text(image):
    w, _ = image.size
    text = 'introtorhythm.com'
    font = ImageFont.truetype('./assets/RobotoMono.ttf', 36)
    width = font.getlength(text)
    text_start = (w - width) // 2

    img_rotate_right = image.rotate(90)
    image_draw = ImageDraw.Draw(img_rotate_right)
    image_draw.text((text_start, 60), text, '#fff', font=font)

    img_rotate_left = img_rotate_right.rotate(180)
    image_draw = ImageDraw.Draw(img_rotate_left)
    image_draw.text((text_start, 60), text, '#fff', font=font)

    image = img_rotate_left.rotate(90)

    return image


def add_show_details(image, show_title, date, start_time, end_time):
    w, h = image.size
    what = show_title
    font = ImageFont.truetype('./assets/RobotoMono.ttf', 60)
    width = font.getlength(what)
    text_start = (w - width) // 2
    text_bottoms_up = (h - 150)
    image_draw = ImageDraw.Draw(image)
    image_draw.text((text_start, text_bottoms_up), what, '#fff', font=font)

    when = f'{date} {start_time}-{end_time} PDT'
    font = ImageFont.truetype('./assets/RobotoMono.ttf', 30)
    width = font.getlength(when)
    text_start = (w - width) // 2
    text_bottoms_up = (h - 70)
    image_draw.text((text_start, text_bottoms_up), when, '#fff', font=font)

    return image


def generate_random_color():
    r = random.randint(0, 99)
    g = r - random.randint(0, 4) if r > 10 else r + random.randint(0, 4)
    b = r + random.randint(0, 4) if r < 90 else r - random.randint(0, 4)

    chance = random.randint(0, 2)

    if chance == 0:
        return f'#{r}{g}{b}'
    elif chance == 1:
        return f'#{g}{b}{r}'
    else:
        return f'#{b}{r}{g}'