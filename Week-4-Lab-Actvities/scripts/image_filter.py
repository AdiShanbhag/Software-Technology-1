from PIL import Image, ImageFilter

# create an image 
image = Image.open('Assignment-2-Activity-1/Assets/Insects/2_Sphaer 2021_1_2021_06_03-11-22-54-873.png')

# apply a basic filter
image_blur = image.filter(ImageFilter.BLUR)
#image_blur.show()

image_contour = image.filter(ImageFilter.CONTOUR)
#image_contour.show()

image_emboss = image.filter(ImageFilter.EMBOSS)
#image_emboss.show()

image_edge = image.filter(ImageFilter.FIND_EDGES)
#image_edge.show()

# apply advanced filters
image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 20))
image_gaussianblur = image.filter(ImageFilter.GaussianBlur(radius = 20))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius = 20))

# image_boxblur.show()
# image_gaussianblur.show()
image_unsharp.show()

image_blur.save('image_blur.png', 'png')
image_emboss.save('image_emboss.png', 'png')
image_edge.save('image_edge.png', 'png')

image_boxblur.save('image_boxblur.png', 'png')
image_gaussianblur.save('image_gaussianblur.png', 'png')
image_unsharp.save('image_unsharp.png', 'png')