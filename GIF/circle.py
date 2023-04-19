from PIL import Image, ImageDraw

images = []

width = 200
center = width // 2
color_1 = (255, 255, 255)
color_2 = (0, 0, 0)
max_radius = int(center * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
    images.append(im)

images[0].save(
    'pillow_imagedraw.gif',
    save_all=True,
    append_images=images[1:],
    optimize=False,
    duration=40,
    loop=0
)
