from xml.dom import minidom
import numpy as np

def classic_kNN(trainset, testset, k, normalize = False, leverage = False, show_progress = False):
    res = []
    tick = 0

    # Normalize
    if normalize:
        temp_train = np.zeros(trainset.shape[0])
        for i in range(0,6):

            max_val = np.max(trainset[:, i])
            min_val = np.min(trainset[:, i])

            normalized = (trainset[:, i]-min_val)/(max_val-min_val)
            temp_train = np.vstack((temp_train, normalized))

        temp_train = temp_train[1:,:].T
        trainset = np.hstack((temp_train, trainset[:,6].reshape(-1,1)))

        temp_test = np.zeros(testset.shape[0])
        for i in range(0,6):

            max_val = np.max(testset[:, i])
            min_val = np.min(testset[:, i])

            normalized = (testset[:, i]-min_val)/(max_val-min_val)
            temp_test = np.vstack((temp_test, normalized))

        temp_test = temp_test[1:,:].T
        testset = np.hstack((temp_test, testset[:,6].reshape(-1,1)))

    # LOOP
    for test in testset:
        # Find k-Nearest Neighbor
        nearest = [[None, 999999] for _ in range(k)]
        for train in trainset:
            distance = np.sum((train-test)**2)**(1/2)
            if distance < nearest[k-1][1]:
                nearest.pop(k-1)
                nearest.append([train, distance])
                nearest.sort(key = lambda x: x[1])        

        # Guess
        neigh_satis = 0
        neigh_unsatis = 0

        if leverage:
            max_distance = max(nearest, key=lambda x: x[1])[1]
            min_distance = min(nearest, key=lambda x: x[1])[1]

            for neighbor in nearest: neighbor[1] = (neighbor[1]-min_distance)/(max_distance-min_distance)
            middle_value = nearest[int(k/2)][1]
            gab = 1 - middle_value
            for neighbor in nearest: neighbor[1] += gab
            for neighbor in nearest: neighbor[1] = 2 - neighbor[1]

            for neighbor in nearest:
                if neighbor[0][6] == 1: 
                    neigh_satis += neighbor[1]
                else               : 
                    neigh_unsatis += neighbor[1]

            if neigh_satis > neigh_unsatis: guess_result = 1
            else                          : guess_result = 0

        else:
            nearest = [n for n,d in nearest]
            for neighbor in nearest:
                
                if neighbor[6] == 1: neigh_satis+=1
                else               : neigh_unsatis+=1

            if neigh_satis > neigh_unsatis: guess_result = 1
            else                          : guess_result = 0

        res.append((test, guess_result))

        # DEBUG
        tick += 1
        if show_progress: 
            if tick%100 == 0: print("now in %dth test data"%tick)
        pass

    return res

def analyze(res):
    count = 0
    for line in res:
        real = int(line[0][6])
        guess = line[1]
        if real == guess: count+=1
    print("accuracy: %6f"%(count/len(res)))
    

###################

import time

data = np.loadtxt("satisfaction_data.csv", delimiter=",", dtype=np.float32)
#np.random.shuffle(data)
trainset = data[:18000]
testset = data[18000:]

small_trainset = testset[:1800]
small_testset = testset[1800:]

print("start")
s = time.time()
res = classic_kNN(small_trainset, small_testset, 5, normalize = True, leverage=False, show_progress=False)
e = time.time()
print("end")

analyze(res)
print("time: %6f sec"%(e-s))