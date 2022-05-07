import numpy as np


a = [[3,1], [6,9], [4,7], [3,3], [13,2]]
a.sort(key = lambda x: x[1])
print(a)

a = [y for x,y in a]
print(a)