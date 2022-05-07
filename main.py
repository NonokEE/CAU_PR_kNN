import sys
import numpy as np
from kNN import kNN, get_accuracy

dataset = []
NUM_DATASET = 1
K_VALUE = 3

for i in range(NUM_DATASET):
    name = "./dataset/dataset" + str(i+1)
    train = np.loadtxt(name+"_train.csv", delimiter= ",")
    test = np.loadtxt(name+"_train.csv", delimiter= ",")

    dataset.append((train, test))

resultset = []
for i in range(NUM_DATASET):
    print(str(i+1) + "th dataset")
    resultset.append(kNN(dataset[i][0], dataset[i][1], K_VALUE, show_progress=True))

path = "./k" + str(K_VALUE) + "/"
for i in range(NUM_DATASET):
    name = path + "result" + str(i+1) + ".csv"
    np.savetxt(name+"_result.csv", resultset[i], delimiter= ",")

accuracy = np.array([[i+1 for i in range(NUM_DATASET)], [0 for _ in range(NUM_DATASET)]])
for i in range(NUM_DATASET):
    accuracy[i][1] = get_accuracy(resultset[i])
np.savetxt(path+"accuracy.csv", accuracy, delimiter= ",")