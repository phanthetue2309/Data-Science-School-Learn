import pandas as pd
import numpy as np
class Murder : 
    def __init__(self,state,population, murderRate,abbreviation):
        self.state = state
        self.population = population
        self.murderRate = murderRate
        self.abbreviation = abbreviation
    def __repr__(self):
        return str(dict({
            "state": self.state,
            "population" : self.population,
            "murderRate" : self.murderRate,
            "abbreviation": self.abbreviation,
        }))

murder = []
dic_murder = dict()

data_excel = pd.read_excel('state.xlsx')
print(data_excel)
df = pd.DataFrame(data_excel)   
rows = df.shape[0]  # số hàng có trong file excel 

for i in range(0,rows):
    murder.append(Murder(state = df.loc[i][0], population = float(df.loc[i][1]), 
        murderRate= float(df.loc[i][2]), abbreviation=df.loc[i][3])) # add to list 
    dic_murder[df.loc[i][1]] =  Murder(state = df.loc[i][0], population = float(df.loc[i][1]), 
        murderRate= float(df.loc[i][2]), abbreviation=df.loc[i][1])

sum_mean = sum_weigth_mean = sum_weight = 0 
count = len(murder)

murderRate = []
population = []

for murder in dic_murder:
    sum_mean += dic_murder[murder].murderRate
    sum_weigth_mean += dic_murder[murder].murderRate * dic_murder[murder].population
    sum_weight += dic_murder[murder].population
    murderRate.append(dic_murder[murder].murderRate)
    population.append(dic_murder[murder].population)

murderRate.sort()

murder2 = murderRate[5:45]
sum_murder2 = sum(murder2)

mean = sum_mean / count
print("mean = ", sum_mean / count) 
print("weight_mean =", sum_weigth_mean / sum_weight) # bang ti le giet nguoi * dan so cua bang / tong dan so 
print("trimmed = " ,sum_murder2 / (count - 10))  # de ra theo ti le %  bo di 10 % du lieu ko can thiet 
print("median = ", (murderRate[count // 2] + murderRate[count // 2 - 1]) / 2) # neu n la so le voi n la so chan 

sum_mean_absolute_deviation = 0

for murder in dic_murder:
    sum_mean_absolute_deviation += abs(dic_murder[murder].murderRate - mean)

mean_absolute_deviation = sum_mean_absolute_deviation / count

print("mean_absolute_deviation = ", mean_absolute_deviation)

mean_population = sum(population) / len(population)
sum_MAD = 0 
for i in range(0,len(population)):
    sum_MAD += abs(population[i] - mean_population)
print("MAD Population = ",sum_MAD / len(population))
# MAD độ lệch tuyệt đối trung bình
# Độ lệch chuẩn (standard devitation) =  sqrt(phương sai)
# phương sai (variance) = (x[i] - x(ngang)) ^ 2 / (n-1)
population.sort()

mid = int(count) // 2

Q1 = population[mid // 2]
Q3 = population[(mid // 2) + mid ]

# 1 2 3 4 5 6 

Q1_new = np.percentile(population, 25)
Q3_new = np.percentile(population, 75)

print("IQR Population = ", Q3 - Q1)
print("IQR Percentile = ", Q3_new - Q1_new)