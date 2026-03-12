from PIL import Image, ImageOps

# create an image
image = Image.open('Assignment-2-Activity-1/Assets/Insects/2_Sphaer 2021_1_2021_06_03-11-22-54-894.png')

# position changes 
image_mirror = ImageOps.mirror(image)
image_scale = ImageOps.scale(image, 0.5)

# color changes 
image_inverted = ImageOps.invert(image_mirror)
image_inverted.save('image_inverted.png', 'png')

# add and remove 
image_border = ImageOps.expand(
	image = image_inverted, 
	border = 50,
	fill = (255,255,255))

image_border.save('image_border.png', 'png')

image_padded = ImageOps.pad(image, (4000,6000))
image_padded.save('image_padded.png', 'png')

image_crop = ImageOps.crop(image = image, border = 200)
image_crop.save('image_crop.png.png', 'png')
image_border.show()