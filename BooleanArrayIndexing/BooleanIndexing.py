import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt

# read the image
imageHere = scipy.ndimage.imread('../nature.jpg')
imageHere1 = scipy.ndimage.imread ('../nature.jpg')

def get_indices(size):
    arr = np.arange (size)
    return arr % 4 == 0

xindices = get_indices (imageHere.shape[0])
yindices = get_indices (imageHere.shape[1])

imageHere[np.ix_(xindices, yindices)] = 0

plt.imshow (imageHere)

# copy the image
imageHere2 = imageHere.copy()
imageHere2[(imageHere > imageHere.max() / 4) & (imageHere < 3 * imageHere.max()) / 4] = 0

plt.subplot (212)
plt.imshow (imageHere2)
plt.show()