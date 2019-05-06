import scipy.ndimage
import matplotlib.pyplot as plt
import numpy as np

# read the image
imageHere = scipy.ndimage.imread ('../nature.jpg')
xmax = imageHere.shape[0]
ymax = imageHere.shape[1]

# create a function to shuffle
def shuffle_indices (size):
    arr = np.arange(size)
    np.random.shuffle (arr)
    return arr

xindices = shuffle_indices (xmax)
np.testing.assert_equal(len(xindices), xmax)

yindices = shuffle_indices (ymax)
np.testing.assert_equal(len (yindices), ymax)

plt.imshow (imageHere[np.ix_(xindices, yindices)])
plt.show ()