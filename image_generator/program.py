from PIL import Image
import functions as f


size = 850
border = 1200

# get colors
primary_color = f.generate_random_color()

# open the primary image (used in background)
background = f.resize_image(Image.open(r"./assets/sean.png").convert('RGB'), size)

# open the secondary image (overlay image)
foreground = f.resize_image(Image.open(r"./assets/play-circle.png"), size)

# paste foreground image on top of background
# starting at coordinates (0, 0)
background.paste(foreground, (0,0), mask = foreground)
image = f.crop_to_circle(background)

output = Image.new("RGB", (border, border), primary_color)
center = (border - size) // 2
output.paste(image, (center, center), mask = image)

# add text
output = f.add_title_with_text(output)
output = f.add_url_text(output)
output = f.add_show_details(output, 'SPIE', '12-15-2022', '5pm', '7pm')

# save the image
output.save(r"./assets/output.png", quality=100)
