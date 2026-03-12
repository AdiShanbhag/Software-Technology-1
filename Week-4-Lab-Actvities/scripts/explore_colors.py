from PIL import Image
image = Image.open('Assignment-2-Activity-1/Assets/Insects/2_Sphaer 2021_1_2021_06_03-11-22-54-873.png')

# get one pixel
print(image.getpixel((0,0)))

# # grayscale images
red_grayscale_image = image.getchannel('R')
#red_grayscale_image.show()

blue_grayscale_image = image.getchannel('B')
#blue_grayscale_image.show()

# change the pixel color
image.putpixel((0,0), (255,0,255))
#image.show()

# explore
print(image.getpixel((0,0)))
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x,y))[0] == 0:
            image.putpixel((x,y), (200,20,20))
image.show()

image.save('explore_colors.png', 'png')