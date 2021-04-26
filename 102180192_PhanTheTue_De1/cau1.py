from random import random
from prettytable import PrettyTable
import numpy as np

list_random = []
for i in range(0,1000):
    list_random.append(random())

print("10 data first : ")
for i in range(0,10):
    print(list_random[i])

def mean(x):
    sum_mean = 0 
    for i in x : 
        sum_mean += i 
    mean = sum_mean / len(x)
    return mean 
    
def median(x):
    x.sort()
    x_mean1 = x[int(len(x) // 2) - 1]
    x_mean2 = x[int(len(x) / 2)]
    return (x_mean1 +  x_mean2) /2
min_list =min(list_random)
print("min = " ,min_list)

max_list =max(list_random)
print("max = " ,max_list)

range_list = str(min_list) + " - " + str(max_list) 
print("range = " ,range_list)

mean_list = mean(list_random)
print("mean = " ,mean_list)

median_list = median(list_random)
print("median = " ,median_list)



n = 20
part = (max_list - min_list) / n
arr_part = []
for i in range(1,n):    # there is n - 1 variable 
    arr_part.append(min_list + part * i) # list of part


str_arr_part = [''] * n
str_arr_part[0] = str(min_list) + "-" + str(arr_part[0])
for i in range(1,n-1):
    str_arr_part[i] = str(arr_part[i-1] )+ "-"+ str( arr_part[i])
str_arr_part[n-1] = str( arr_part[n-2] ) + "-" + str(arr_part[n-2] + part ) 

arr_count = np.zeros(n)  # tạo biến đếm số lượng
for i in range(0, 1000):
    for j in range(0,n-1):
        if (list_random[i] < arr_part[j]) :
            arr_count[j] += 1
            break
        
arr_count[n-1] = 1000 - sum(arr_count)

t = PrettyTable(['BinRange','Frequency'])
for i in range(0,n):
    t.add_row([str_arr_part[i],int(arr_count[i])])
print(t)

print("Phan bo deu")
