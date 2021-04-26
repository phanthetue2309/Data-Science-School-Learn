# Python Program illustrating 
# numpy.percentile() method 

import numpy as np

# 1D array 
arr = [20,3,43,92,41,55,98,32,25,69]
samples = sorted([1,4,5,31,41,44,49,51,54,98])
print("arr : ", arr) 
arr.sort()
print(arr)
print("50th percentile of arr : ", 
	np.percentile(arr, 50))
print("25th percentile of arr : ",
	np.percentile(arr, 25))
print("75th percentile of arr : ",
	np.percentile(arr, 75))
print(np.percentile(arr, 75) - np.percentile(arr, 25))

import math

def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

p5 = percentile(samples, 5)
p25 = percentile(samples, 25)
p50 = percentile(samples, 50)
p75 = percentile(samples, 75)
p95 = percentile(samples, 95)

print(p75)