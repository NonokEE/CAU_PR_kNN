import numpy as np

def classic_kNN(trainset, testset, k, show_tick = True):
    res = []
    tick = 0

    for test in testset:
        # Find k-Nearest Neighbor
        nearest = [(None, 99999) for _ in range(k)]
        for train in trainset:
            distance = np.sum((train-test)**2)**(1/2)
            if distance < nearest[k-1][1]:
                nearest.pop(k-1)
                nearest.append((train, distance))
                nearest.sort(key = lambda x: x[1])

        # Guess
        nearest = [n for n,d in nearest]
        neigh_satis = 0
        neigh_unsatis = 0

        for neighbor in nearest:
            
            if neighbor[6] == 1: neigh_satis+=1
            else               : neigh_unsatis+=1

        if neigh_satis > neigh_unsatis: guess_result = 1
        else                          : guess_result = 0

        res.append((test, guess_result))

        # DEBUG
        tick += 1
        if show_tick: 
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
trainset = data[:18000]
testset = data[18000:]

small_trainset = testset[:1800]
small_testset = testset[1800:]



print("start")
s = time.time()
res = classic_kNN(trainset, testset, 5)
e = time.time()
print("end")

analyze(res)
print("time: %6f sec"%(e-s))
