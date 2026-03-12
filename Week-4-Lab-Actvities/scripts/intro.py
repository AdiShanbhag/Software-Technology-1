from PIL import Image

# create an image via import
image = Image.open('Assignment-2-Activity-1/Assets/Insects/2_Sphaer 2021_1_2021_06_03-11-22-54-873.png')

# analyze the image
print(image.size)
print(image.filename)
print(image.format)

#image.show()

# flip the image
image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# show the image
#image.show()

# exercise
img_rotated = image.rotate(30)
img_rotated.save('roated_insect_3.png', 'png')
image.show()