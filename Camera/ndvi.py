import cv2
import numpy as np
from fastiecm import fastiecm

original = cv2.imread('./pictures/image_02_05_2022_17_02_55.jpg') # Load image from /images/

"""def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)  # Convert to an array of pixels
    
    shape = image.shape # get image shape
    
    height = int(shape[0]/3) # image height displayed on screen
    width = int(shape[1]/3) # image width displayed on screen
    
    image = cv2.resize(image, (width, height)) # resize the image
    
    # creates a window with the image displayed
    
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""
    
def contrast_stretch(im):
    # The next step is to find the largest and smallest of those numbers
    
    in_min = np.percentile(im, 5) # find the top 5% brightness of pixels in the image
    in_max = np.percentile(im, 95) # find the bottom 5% brightness of pixels in the image

    out_min = 0.0 # lowest possible brightness
    out_max = 255.0 # highest possible brightness
    
    # increases the constrast
    
    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min 

    return out # returns the contrasted image


def calc_ndvi(image):
    b, g, r = cv2.split(image) # split in to the rgb channels
    
    # NDVI = (NIR – Red) / (NIR + Red)
    
    # The red and blue channels need to be added together and stored as bottom.
    # The blue channel can then have the red channel subtracted and then divided by the bottom calculation.
    
    # Because we’re doing a division, we also need to make sure that none of our divisors are 0, or there will be an error.
    
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b) / bottom
    
    return ndvi
    

contrasted = contrast_stretch(original) # contrast the original image

cv2.imwrite('results/contrasted.png', contrasted) # saves the contrasted image to a file

ndvi = calc_ndvi(contrasted) # calculates the ndvi with the contrasted image

cv2.imwrite('results/ndvi.png', ndvi) # saves the ndvi image to a file

ndvi_contrasted = contrast_stretch(ndvi) # enhance the image

cv2.imwrite('results/ndvi_contrasted.png', ndvi_contrasted) # saves the ndvi contrasted image to a file

#display(original, 'Original')
#display(contrasted, 'Contrasted original')
#display(ndvi, 'NDVI')
#display(ndvi_contrasted, 'NDVI Contrasted')

# Because it’s difficult for humans to tell the difference between different shades of grey. We can run the image through a colour mapping process that will turn really bright pixels to the colour red and dark pixels to the colour blue. 

# The image is greyscale which means that each pixel can be represented by a single number from 0 to 255.

# The fastie colour map takes dark pixels and makes them white. Then the brighter the original pixels, the further along the spectrum the colours are shifted. So dark grey pixels become blue, while bright white pixels become red.

color_mapped_prep = ndvi_contrasted.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)

cv2.imwrite('results/color_mapped_image.png', color_mapped_image)

#display(color_mapped_image, 'Color mapped')

