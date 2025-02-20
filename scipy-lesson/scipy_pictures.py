import numpy as np
from matplotlib import pyplot as plt

random_image = np.random.random([500, 500])

plt.imshow(random_image, cmap='RdPu_r', interpolation='hermite')
plt.show()
# -------------------------------------------
print("Робота з зображеннями \n")
im = plt.imread("image.jpg")
plt.imshow(im)
print(im.shape)
plt.title("First picture \n")
plt.show()
# ------------------------------------

y = im.shape[0]
x = im.shape[1]
h = 7
w = (y/x) * h
plt.figure(figsize=(w, h))
plt.imshow(im)
plt.title("Second picture \n")
plt.show()
# ----------------------------------------

y = im.shape[0]
x = im.shape[1]
h = 7
w = (y/x) * h
plt.figure(figsize=(w, h))
plt.imshow(im[200:700, 100:650, :])
plt.title("Third picture \n")
plt.show()
# ---------------------------------------

y = im.shape[0]
x = im.shape[1]
h = 3
w = (y/x) * h
plt.figure(figsize=(w,h))
plt.imshow(im)
plt.title("Fourth picture \n")
plt.show()
# ---------------------------------------

y = im.shape[0]
x = im.shape[1]
h = 7
w = (y/x) * h
plt.figure(figsize=(w,h))
plt.imshow(im[200:700, 100:650, :])
# plt.imshow(1 - im[200:700, 100:650, :]) # отримання негативу
# plt.imshow(np.mean(im[200:700, 100:650, :], axis=2), cmap='gist_gray') # знебарвлення 
# plt.savefig("test.jpg") #  збереження малюнку

# im_flipud = np.flipud(im[200:700, 100:650, :]) # перевертання малюнку
# plt.imshow(im_flipud) # перевертання малюнку
plt.show()
# ---------------------------------------

