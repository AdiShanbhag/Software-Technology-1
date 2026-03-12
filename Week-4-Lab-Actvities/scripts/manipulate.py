#manipulate.py
from PIL import Image

# import an image
image = Image.open('Assignment-2-Activity-1/Assets/Insects/2_Sphaer 2021_1_2021_06_03-11-22-54-894.png')

# flip
image_transpose = image.transpose(Image.Transpose.ROTATE_90)

# rotation
image_rotate = image.rotate(45, expand = False, center = (0,0))

# crop
image_crop = image.crop((800,600,1600,1600))

# resize
image_resize = image.resize((1000,600))

# applying multiple transformations to an image in a single line of code
combined_image = image.transpose(Image.Transpose.ROTATE_90).resize((2000,1500)).rotate(10).crop((700, 300, 1500, 1500))
combined_image.show()

combined_image.save('manipulated.png', 'png')