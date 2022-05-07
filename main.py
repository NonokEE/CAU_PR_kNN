import sys
import numpy as np
from kNN import kNN, get_accuracy

TRAIN_PATH = sys.argv[1]
TEST_PATH = sys.argv[2]
K_VALUE = int(sys.argv[3])
SHOW_PROCESS = bool(sys.argv[4])

train = np.loadtxt(TRAIN_PATH, delimiter= ",")
test = np.loadtxt(TEST_PATH, delimiter= ",")
result = kNN(train, test, K_VALUE, show_process=SHOW_PROCESS)
np.savetxt("result.csv", result, delimiter= ",")