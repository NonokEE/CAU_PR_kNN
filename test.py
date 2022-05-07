from matplotlib.pyplot import axis
import numpy as np

train = np.array([1,2,3,4,5])
test = np.array([10,11,12,13,14])


print(np.sum((train-test)**2)**(1/2))