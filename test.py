import numpy as np

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [1,5,9]])
test = []

newa = a.copy()
np.random.shuffle(newa)
test.append(newa[0])

newa = a.copy()
np.random.shuffle(newa)
test.append(newa[0])
newa = a.copy()
np.random.shuffle(newa)
test.append(newa[0])
newa = a.copy()
np.random.shuffle(newa)
test.append(newa[0])
newa = a.copy()
np.random.shuffle(newa)
test.append(newa[0])


print(test)