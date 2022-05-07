import numpy as np

a = [[1,4], [2,5], [3,6], [4,7], [5,8]]

maxval = max(a, key = lambda x:x[1])[1]
minval = min(a, key = lambda x:x[1])[1]

print(maxval)
print(minval)

for i in a: i[1] = (i[1]-minval)/(maxval-minval)
middle_value = a[int(len(a)/2)][1]
gab = 1 - middle_value
for i in a: i[1] += gab

print(a)