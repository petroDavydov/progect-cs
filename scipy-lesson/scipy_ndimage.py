from scipy import ndimage
import matplotlib.pyplot as plt

print("SciPy Ndimage - робота з малюнками \n")
im = plt.imread("image.jpg")
rotate_face = ndimage.rotate(im, -45)

plt.imshow(rotate_face)
plt.title("First Image \n")

plt.show()
# ---------------------------------------


im = plt.imread("image.jpg")[200:700, 100:650, :]
blurred_im_2 = ndimage.gaussian_filter(im, sigma=2)
blurred_im_4 = ndimage.gaussian_filter(im, sigma=4)

fig, axs = plt.subplots(1, 3, figsize=(50, 100))

axs[0].imshow(im)
axs[1].imshow(blurred_im_2)
axs[2].imshow(blurred_im_4)

axs[0].set_title("Розмиття країв малюнку - no blured \n")
axs[1].set_title("Розмиття країв малюнку - blured_im_2:  \n")
axs[2].set_title("Розмиття країв малюнку - blured_im_3:  \n")

plt.show()
# ----------------------------------------------

