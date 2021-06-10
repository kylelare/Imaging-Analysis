import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('messi5.jpg')

#plotting original image
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()

#discrete fourier transform on image
ft = np.fft.fft2(image)
ftshift = np.fft.fftshift(ft)
magspectrum = 20*np.log(np.abs(ftshift))

#plotting spectrum
plt.imshow(magspectrum.astype('uint8'), cmap='gray')
plt.axis('off')
plt.show()
