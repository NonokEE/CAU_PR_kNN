import numpy as np

def classic_kNN(trainset, testset, k=3, howmuch = True):
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
        if howmuch: 
            if tick%100 == 0: print("now in %dth test data"%tick)
        pass

    return res

    
    

data = np.loadtxt("satisfaction_data.csv", delimiter=",", dtype=np.float32)
trainset = data[:18000]
testset = data[18000:]

small_trainset = testset[:1800]
small_testset = testset[1800:]

print("start")
res = classic_kNN(small_trainset, small_testset)
print("end")

for i in range(len(res)):
    print(res[i][0][6], res[i][1])