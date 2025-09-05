import numpy as np
arr = np.array([2, 4, 5, 7, 3, 8, 1, 9])
target = 10

pairs = []

for i in np.arange(len(arr)):
    for j in np.arange(i+1, len(arr)):        
        if arr[i] + arr[j] == target:
            pair = sorted([arr[i], arr[j]])
            if pair not in pairs:
                pairs.append(pair)
            

pairs = np.array(pairs)
print(pairs)