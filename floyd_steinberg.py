import imageio
import numpy as np
import matplotlib.pyplot as plt


# Floyd-Steinberg dithering
# img: image as numpy array in grayscale, values in [0,255]
def floyd_steinberg(img):
    height, width = img.shape
    result = np.pad(img, (1,1), 'constant')
    for y in range(height):
        for x in range(width):
            value = 255 * (result[y+1,x+1] > 127)
            error = result[y+1,x+1] - value
            result[y+1,x+2] += int(error * 7 / 16)
            result[y+2,x] += int(error * 3 / 16)
            result[y+2,x+1] += int(error * 5 / 16)
            result[y+2,x+2] += int(error * 1 / 16)
            result[y+1,x+1] = value
    return result[1:height+1, 1:width+1]


def plt_gray(image, title):
    plt.xlabel(title)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap='gray')


def plt_color(image, title):
    plt.xlabel(title)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image)


downsample = 3
color = imageio.imread('imageio:astronaut.png')[::downsample,::downsample,:]

gray = np.mean(color, axis=2)
bw_nearest = 255 * (gray > 127)
bw_dither = floyd_steinberg(gray)

red = color[:,:,0]
green = color[:,:,1]
blue = color[:,:,2]
color_nearest = np.stack([255 * (red > 127),
                          255 * (green > 127),
                          255 * (blue > 127)], axis=2)
color_dither = np.stack([floyd_steinberg(red),
                         floyd_steinberg(green),
                         floyd_steinberg(blue)], axis=2)

plt.figure('Floyd-Steinberg dithering')

plt.subplot(231)
plt_gray(bw_nearest, 'b/w nearest')

plt.subplot(232)
plt_gray(gray, 'grayscale')

plt.subplot(233)
plt_gray(bw_dither, 'b/w dithering')

plt.subplot(234)
plt_color(color_nearest, 'color nearest')

plt.subplot(235)
plt_color(color, 'color')

plt.subplot(236)
plt_color(color_dither, 'color dithering')

plt.show()
