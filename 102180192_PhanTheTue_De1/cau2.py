import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data1 = np.random.normal(100,20,1000)

data2 = np.random.normal(50,10,1000)

data3 = data1 + data2

mean_data1 = np.mean(data1)
print("trung binh mau data1 =" ,mean_data1)
mean_data3 = np.mean(data3)
print("trung binh mau data3 =" ,mean_data3)

standard_data1 = np.std(data1)
print("Do lech chuan mau data1 =" ,standard_data1)
standard_data3 = np.std(data3)
print("Do lech chuan mau data3 =" ,standard_data3)

data = {'a': data1, 
'c': np.random.randint(0, 1000, 1000),
'd': np.random.randn(1000)}
data['b'] = data3
data['d'] = np.abs(data['d']) * 100
plt.scatter('a', 'b', data=data)  
plt.xlabel('Data 1')
plt.ylabel('Data 3')
plt.show()

