from PIL import Image

frames = []

for frame_number in range(1, 11):
    frame = Image.open(f'images/homer-{frame_number}.jpg')
    frames.append(frame)

frames[0].save(
    'homer.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=100,
    loop=0
)
