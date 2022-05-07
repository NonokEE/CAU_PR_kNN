import numpy as np

data = np.loadtxt("satisfaction_data.csv", delimiter=",")
print(data.shape)

dataset = []
for _ in range(10):
    temp = data.copy()
    np.random.shuffle(temp)
    train_set = temp[:18000]
    test_set = temp[18000:]
    dataset.append((train_set, test_set))

for i in range(len(dataset)):
    name = "dataset" + str(i+1)
    np.savetxt(name+"_train.csv", dataset[i][0], delimiter= ",")
    np.savetxt(name+"_test.csv", dataset[i][1], delimiter= ",")
