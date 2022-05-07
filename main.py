import sys
import numpy as np
from kNN import kNN, get_accuracy

TRAIN_PATH = sys.argv[1]
TEST_PATH = sys.argv[1]
K_VALUE = sys.argv[1]
SHOW_PROCESS = sys.argv[1]

train = np.loadtxt(TRAIN_PATH, delimiter= ",")
test = np.loadtxt(TEST_PATH, delimiter= ",")
result = kNN(train, test, K_VALUE, show_progress=SHOW_PROCESS)

    resultset.append(kNN(dataset[i][0], dataset[i][1], K_VALUE, show_progress=True))

path = "./k" + str(K_VALUE) + "/"
for i in range(NUM_DATASET):
    name = path + "result" + str(i+1) + ".csv"
    np.savetxt(name+"_result.csv", resultset[i], delimiter= ",")

accuracy = np.array([[i+1 for i in range(NUM_DATASET)], [0 for _ in range(NUM_DATASET)]])
for i in range(NUM_DATASET):
    accuracy[i][1] = get_accuracy(resultset[i])
np.savetxt(path+"accuracy.csv", accuracy, delimiter= ",")