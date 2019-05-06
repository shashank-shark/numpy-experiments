from scipy import misc
import matplotlib.pyplot as plt

# read the image
imageHere = misc.imread ('nature.jpg')

# get the max ranges of pixels in x * y
xmax = imageHere.shape[0]
ymax = imageHere.shape[1]

print (xmax)
print (ymax)

# use the iterator object of numpy
imageHere [range(xmax), range(ymax)] = 0
imageHere [range(xmax - 1, -1, -1), range (ymax - 1, -1, -1)] = 0

# for let-top to right-bottom image
# for i in range(xmax):
#     for j in range(ymax):
#         imageHere[i,j] = 0

plt.imshow (imageHere)
plt.show()